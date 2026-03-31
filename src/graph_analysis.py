import os
import itertools
from collections import Counter
import matplotlib.patches as mpatches

# Data manipulation and parsing
import polars as pl
import jsonpickle

# Graph and Network Analysis
import networkx as nx
import community.community_louvain as community_louvain
import matplotlib.pyplot as plt

# IMPORTANT: We import your custom classes so jsonpickle knows how to decode the strings
from definition.data.MatchedAuthorData import MatchedPaperData


def load_and_build_graph(parquet_filename: str) -> nx.Graph:
    """
    Reads the processed parquet file and builds a co-affiliation network graph.
    Nodes = Authors
    Edges = Shared Institutions (weighted by how many times they share one)
    """
    print(f"Loading data from {parquet_filename}...")

    if not os.path.exists(parquet_filename):
        raise FileNotFoundError(f"Could not find {parquet_filename}. Make sure it is in the same folder.")

    # 1. Load data and filter out failed matches
    df = pl.read_parquet(parquet_filename)
    df_matched = df.filter(pl.col("matched_info").is_not_null())

    # 2. Build the Bipartite Mapping (Institution ROR ID -> Set of Author Names)
    # This is much faster than comparing every author to every other author.
    institution_to_authors = {}

    print("Decoding JSON and grouping authors by institution...")
    for json_str in df_matched["matched_info"]:
        try:
            # Convert the string back into your MatchedPaperData Python object
            paper_data: MatchedPaperData = jsonpickle.decode(json_str)

            for author in paper_data.matched_authors:
                author_name = author.arxiv_name

                for affil in author.affiliations:
                    inst_id = affil.matched_ror.ror_id

                    # Add the author to the institution's "bucket"
                    if inst_id not in institution_to_authors:
                        institution_to_authors[inst_id] = set()
                    institution_to_authors[inst_id].add(author_name)

        except Exception as e:
            print(f"Warning: Failed to parse a row: {e}")
            continue

    # --- NEW CODE TO PRINT BUCKETS ---
    print("\n--- Sneak Peek at the 'Buckets' (Institutions -> Authors) ---")

    # We use a counter to only print the first 5 buckets so we don't crash the terminal
    bucket_count = 0
    for inst_id, authors in institution_to_authors.items():
        if bucket_count >= 5:
            break

        print(f"Bucket [ROR ID: {inst_id}] contains {len(authors)} authors:")
        print(f"  -> {', '.join(authors)}\n")

        bucket_count += 1
        print("-------------------------------------------------------------\n")

    print("Building the network graph edges...")
    G = nx.Graph()

    for inst_id, authors in institution_to_authors.items():
        # itertools.combinations creates pairs of every author in this institution
        for author_a, author_b in itertools.combinations(authors, 2):
            if G.has_edge(author_a, author_b):
                # If they already have an edge, increase the connection strength
                G[author_a][author_b]['weight'] += 1
            else:
                # First time they are linked, create an edge with weight 1
                G.add_edge(author_a, author_b, weight=1)

    print(
        f"Graph successfully built: {G.number_of_nodes()} Nodes (Authors) and {G.number_of_edges()} Edges (Connections).")
    return G


def analyze_network(G: nx.Graph):
    """
    Calculates Degree Centrality, Betweenness Centrality, and Louvain Communities.
    Returns the community partition and degree dictionary for visualization.
    """
    print("\n--- Running Network Analysis ---")

    # 1. Degree Centrality (Who has the most co-affiliated colleagues?)
    degree_dict = dict(G.degree(weight='weight'))
    top_degree = sorted(degree_dict.items(), key=lambda x: x[1], reverse=True)[:10]

    print("\nTop 10 Central Authors (Highest Degree / Most Connections):")
    for rank, (author, degree) in enumerate(top_degree, 1):
        print(f" {rank}. {author} (Degree: {degree})")

    # 2. Betweenness Centrality (Who bridges different academic groups together?)
    # Note: We calculate this only on the Giant Connected Component to save time.
    gcc_nodes = max(nx.connected_components(G), key=len)
    GCC = G.subgraph(gcc_nodes)

    print("\nCalculating Betweenness Centrality (This might take a moment)...")
    betweenness_dict = nx.betweenness_centrality(GCC, weight='weight')
    top_betweenness = sorted(betweenness_dict.items(), key=lambda x: x[1], reverse=True)[:10]

    print("\nTop 10 'Bridge' Authors (Highest Betweenness Centrality):")
    for rank, (author, score) in enumerate(top_betweenness, 1):
        print(f" {rank}. {author} (Score: {score:.4f})")

    # 3. Community Detection (Finding distinct research cliques/groups)
    print("\nDetecting Academic Communities (Louvain Method)...")
    partition = community_louvain.best_partition(G, weight='weight')

    community_counts = Counter(partition.values())
    print(f"Found {len(community_counts)} distinct communities.")
    print(f"Sizes of the top 5 largest communities: {community_counts.most_common(5)}")

    return partition, degree_dict


def visualize_raw_graph(G: nx.Graph):
    """
    Draws the complete, unfiltered graph immediately after it is built.
    Includes all isolated nodes and disconnected pairs (No GCC filtering).
    """
    print(f"\nGenerating Visualization for the Raw Full Graph ({G.number_of_nodes()} Nodes)...")

    plt.figure(figsize=(12, 12))
    plt.title(f"Raw Author Co-Affiliation Network\n({G.number_of_nodes()} Nodes, {G.number_of_edges()} Edges)",
              fontsize=16, fontweight='bold')

    # Calculate layout for the entire graph
    pos = nx.spring_layout(G, k=0.15, seed=42)

    # Give nodes a basic size based on their connections so hubs still stand out slightly
    degrees = dict(G.degree())
    sizes = [min(degrees[n] * 20 + 30, 400) for n in G.nodes()]

    # Draw edges
    nx.draw_networkx_edges(G, pos, alpha=0.2, edge_color="black")

    # Draw nodes in a uniform color since we haven't calculated communities yet
    nx.draw_networkx_nodes(
        G, pos,
        node_color="#add8e6",  # Light blue
        node_size=sizes,
        alpha=0.9,
        edgecolors="#00008b",  # Dark blue borders
        linewidths=0.8
    )

    plt.axis("off")
    plt.tight_layout()

    print("Opening Raw Graph window. (*** YOU MUST CLOSE THIS WINDOW TO CONTINUE THE SCRIPT ***)")
    plt.show()




def visualize_graph(G: nx.Graph, partition: dict, degree_dict: dict):
    """
    Draws only the Top 4 largest communities.
    Highlights the 'bridge' edges that connect authors from different communities.
    """
    print("\nGenerating Visualization for Top 4 Communities with Bridges...")

    # 1. Count the communities and find the Top 4 largest ones
    community_counts = Counter(partition.values())
    top_4_comms = [comm_id for comm_id, count in community_counts.most_common(4)]

    # 2. Extract ONLY the authors (nodes) that belong to these 4 communities
    top_nodes = [node for node, comm_id in partition.items() if comm_id in top_4_comms]
    SubG = G.subgraph(top_nodes)

    # 3. Assign a specific color to each of the top 4 communities
    color_mapping = {
        top_4_comms[0]: "#1f77b4",  # Blue
        top_4_comms[1]: "#ff7f0e",  # Orange
        top_4_comms[2]: "#2ca02c",  # Green
        top_4_comms[3]: "#d62728",  # Red
    }
    colors = [color_mapping[partition[node]] for node in SubG.nodes()]

    # 4. Calculate sizes based on degree (popularity)
    sizes = [min(degree_dict[node] * 20, 600) for node in SubG.nodes()]

    # 5. Physics simulation for layout
    pos = nx.spring_layout(SubG, k=0.15, seed=42)

    # --- NEW: SEPARATE INTERNAL EDGES FROM BRIDGE EDGES ---
    internal_edges = []
    bridge_edges = []

    # Look at every connection in our filtered graph
    for author_a, author_b in SubG.edges():
        # If they belong to the same community, it's an internal link
        if partition[author_a] == partition[author_b]:
            internal_edges.append((author_a, author_b))
        # If they belong to different communities, it's a bridge!
        else:
            bridge_edges.append((author_a, author_b))

    # 6. Draw the plot
    plt.figure(figsize=(14, 14))
    plt.title("Author Co-Affiliation Network (Top 4 Communities & Bridges)", fontsize=18, fontweight='bold')

    # --- NEW: DRAW EDGES DIFFERENTLY ---
    # Draw internal edges faintly (light gray, very transparent)
    nx.draw_networkx_edges(SubG, pos, edgelist=internal_edges, alpha=0.10, edge_color="black")

    # Draw bridge edges prominently (black, thicker, less transparent)
    nx.draw_networkx_edges(SubG, pos, edgelist=bridge_edges, alpha=0.7, edge_color="black", width=1.5)

    # Draw the dots (nodes)
    nx.draw_networkx_nodes(
        SubG, pos,
        node_color=colors,
        node_size=sizes,
        alpha=0.85,
        edgecolors="white",
        linewidths=0.5
    )

    # Label only the top 15 most connected authors
    top_labeled_nodes = sorted(dict(SubG.degree()).items(), key=lambda x: x[1], reverse=True)[:15]
    labels = {node: node for node, degree in top_labeled_nodes}
    nx.draw_networkx_labels(SubG, pos, labels=labels, font_size=9, font_weight="bold", font_color="black")

    # 7. Add a Professional Legend (Including a marker for Bridges)
    legend_handles = [
        mpatches.Patch(color="#1f77b4", label=f"Community 1 ({community_counts[top_4_comms[0]]} Authors)"),
        mpatches.Patch(color="#ff7f0e", label=f"Community 2 ({community_counts[top_4_comms[1]]} Authors)"),
        mpatches.Patch(color="#2ca02c", label=f"Community 3 ({community_counts[top_4_comms[2]]} Authors)"),
        mpatches.Patch(color="#d62728", label=f"Community 4 ({community_counts[top_4_comms[3]]} Authors)"),
        # Add a line to the legend explaining the black lines
        plt.Line2D([0], [0], color='black', lw=1.5, alpha=0.7, label='Inter-Community Bridge')
    ]
    plt.legend(handles=legend_handles, loc='upper left', title="Network Legend", title_fontsize='13', fontsize='11')

    # Hide the axis and show the plot
    plt.axis("off")
    plt.tight_layout()

    print(f"Found {len(internal_edges)} internal connections and {len(bridge_edges)} bridge connections.")
    print("Opening plot window. (Close the window to end the script).")
    plt.show()






def main():
    # Set up your file paths (Ensure this matches the output of your pipeline)
    INPUT_FILE = "math_sample_processed.parquet"

    try:
        # Step 1: Build the raw graph
        G = load_and_build_graph(INPUT_FILE)

        # Guard clause: Ensure the graph isn't completely empty before analyzing
        if G.number_of_nodes() == 0:
            print("The graph has no nodes! Please check if your parquet file has valid 'matched_info' data.")
            return

        visualize_raw_graph(G)

        # Step 2: Compute the math your professor asked for
        partition, degree_dict = analyze_network(G)

        # Step 3: Draw the final map
        visualize_graph(G, partition, degree_dict)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

