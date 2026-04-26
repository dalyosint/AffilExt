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

    # Load data
    df = pl.read_parquet(parquet_filename)
    # filter out failed matches
    df_matched = df.filter(pl.col("matched_info").is_not_null())

    # Build the Bipartite Mapping (Institution ROR ID -> Set of Author Names)
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


    print("\n--- Sneak Peek at the 'Buckets' (Institutions -> Authors) ---")

    #  print the first 5 buckets
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
    # paring everyone in the bucket
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

    # Sort ALL connected components by size, from largest to smallest
    components = sorted(nx.connected_components(G), key=len, reverse=True)

    # We will analyze up to the top 3 largest components
    # (Using min() just in case the graph is so small it only has 1 or 2 components)
    num_components_to_analyze = min(3, len(components))

    betweenness_dict = {}

    print(f"\nCalculating Betweenness Centrality for the Top {num_components_to_analyze} largest isolated networks...")

    for i in range(num_components_to_analyze):
        comp_nodes = components[i]
        print(f"  -> Processing Component {i + 1} (Contains {len(comp_nodes)} authors)...")

        # Create a subgraph for just this specific component
        subgraph = G.subgraph(comp_nodes)

        # Calculate betweenness just for this component
        comp_betweenness = nx.betweenness_centrality(subgraph, weight='weight')

        # Add these scores into our master dictionary
        betweenness_dict.update(comp_betweenness)

    # Sort the combined dictionary to find the top 10 bridges across ALL the top 3 components
    top_betweenness = sorted(betweenness_dict.items(), key=lambda x: x[1], reverse=True)[:10]

    print("\nTop 10 'Bridge' Authors (Across Top Components):")
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
    nx.draw_networkx_edges(G, pos, alpha=0.4, edge_color="black")

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

    print("Opening Raw Graph window.")
    plt.show()




def visualize_graph(G: nx.Graph, partition: dict, degree_dict: dict):
    """
    Thesis-ready visualization of the top 4 communities with bridges.
    """
    print("\nGenerating Visualization for Top 4 Communities with Bridges...")

    community_counts = Counter(partition.values())
    top_4_comms = [comm_id for comm_id, count in community_counts.most_common(4)]

    top_nodes = [node for node, comm_id in partition.items() if comm_id in top_4_comms]
    SubG = G.subgraph(top_nodes)

    # Colorblind-friendly palette (Okabe-Ito)
    color_mapping = {
        top_4_comms[0]: "#0072B2",
        top_4_comms[1]: "#E69F00",
        top_4_comms[2]: "#009E73",
        top_4_comms[3]: "#D55E00",
    }
    colors = [color_mapping[partition[node]] for node in SubG.nodes()]
    sizes = [min(degree_dict[node] * 18 + 40, 700) for node in SubG.nodes()]

    # Looser layout so communities actually separate visually
    pos = nx.spring_layout(SubG, k=0.45, iterations=100, seed=42)

    internal_edges, bridge_edges = [], []
    for a, b in SubG.edges():
        if partition[a] == partition[b]:
            internal_edges.append((a, b))
        else:
            bridge_edges.append((a, b))

    fig, ax = plt.subplots(figsize=(16, 12))
    ax.set_title("Author Co-Affiliation Network — Top 4 Communities",
                 fontsize=17, fontweight='bold', pad=15)

    nx.draw_networkx_edges(SubG, pos, edgelist=internal_edges,
                           alpha=0.25, edge_color="#888888", width=0.6, ax=ax)
    nx.draw_networkx_edges(SubG, pos, edgelist=bridge_edges,
                           alpha=0.55, edge_color="#333333", width=0.9, ax=ax)

    nx.draw_networkx_nodes(SubG, pos, node_color=colors, node_size=sizes,
                           alpha=0.9, edgecolors="white", linewidths=0.8, ax=ax)

    # Label top 2 authors PER community (spreads labels around, avoids overlap)
    labels = {}
    for comm_id in top_4_comms:
        comm_nodes = [(n, degree_dict[n]) for n in SubG.nodes() if partition[n] == comm_id]
        for n, _ in sorted(comm_nodes, key=lambda x: x[1], reverse=True)[:2]:
            labels[n] = n

    nx.draw_networkx_labels(SubG, pos, labels=labels,
                            font_size=9, font_weight="bold", font_color="black",
                            bbox=dict(facecolor="white", edgecolor="none",
                                      alpha=0.75, pad=1.5), ax=ax)

    legend_handles = [
        mpatches.Patch(color=color_mapping[top_4_comms[i]],
                       label=f"Community {i+1}  (n = {community_counts[top_4_comms[i]]})")
        for i in range(4)
    ]
    legend_handles.append(
        plt.Line2D([0], [0], color='#333333', lw=1.2, alpha=0.7,
                   label=f'Inter-community bridge (n = {len(bridge_edges)})')
    )
    ax.legend(handles=legend_handles, loc='upper left',
              title="Legend", title_fontsize=11, fontsize=10, frameon=True)

    modularity = community_louvain.modularity(partition, G, weight='weight')
    stats_text = (f"Nodes: {SubG.number_of_nodes()}\n"
                  f"Edges: {SubG.number_of_edges()}\n"
                  f"Communities shown: 4 of {len(community_counts)}\n"
                  f"Modularity Q: {modularity:.3f}")
    ax.text(0.99, 0.01, stats_text, transform=ax.transAxes,
            fontsize=9, verticalalignment='bottom', horizontalalignment='right',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='white',
                      edgecolor='#cccccc', alpha=0.9))

    ax.axis("off")
    plt.tight_layout()
    plt.savefig("co_affiliation_network.png", dpi=300, bbox_inches='tight')
    print(f"Saved co_affiliation_network.png — {len(internal_edges)} internal, {len(bridge_edges)} bridge edges.")
    plt.show()

def main():
    # Set up your file paths (Ensure this matches the output of your pipeline)
    INPUT_FILE = "math_sample_processed_final.parquet"

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

