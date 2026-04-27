import os
import itertools
from collections import Counter
import dataclasses
from typing import Dict, List, Union, Set
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

# --- 1. CONNECTED PAPERS-STYLE DATACLASSES ---

InstitutionID = str
Edge = List[Union[InstitutionID, float]]  # [InstitutionID, InstitutionID, weight]


@dataclasses.dataclass
class SharedAuthor:
    """An author who bridges multiple institutions (mimics CommonAuthor)."""
    id: str
    name: str
    institutions: List[InstitutionID]


@dataclasses.dataclass
class InstitutionNode:
    """An institution node in the similarity graph (mimics Paper)."""
    id: InstitutionID
    name: str
    author_count: int
    pos: List[float] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class InstitutionGraph:
    """
    The complete graph structure, modeled after ConnectedPapers Graph.
    """
    nodes: Dict[InstitutionID, InstitutionNode]
    edges: List[Edge]
    shared_authors: List[SharedAuthor]


# --- 2. DATA PROCESSING & GRAPH BUILDING ---

def load_and_build_data_structures(parquet_filename: str) -> InstitutionGraph:
    """
    Reads the parquet file, extracts author-institution relationships,
    and returns a formally structured InstitutionGraph.
    """
    print(f"Loading data from {parquet_filename}...")

    if not os.path.exists(parquet_filename):
        raise FileNotFoundError(f"Could not find {parquet_filename}. Make sure it is in the same folder.")

    df = pl.read_parquet(parquet_filename)
    df_matched = df.filter(pl.col("matched_info").is_not_null())

    # Mapping Author -> Set of Institution ROR IDs
    author_to_institutions: Dict[str, Set[str]] = {}
    # Track unique authors per institution for node sizing
    institution_to_authors: Dict[str, Set[str]] = {}
    # Add a new dictionary at the top of the function to track names
    institution_names: Dict[str, str] = {}
    # Add this dictionary right before the loop
    institution_names: Dict[str, str] = {}

    print("Decoding JSON and mapping cross-institutional authors...")
    for json_str in df_matched["matched_info"]:
        try:
            paper_data: MatchedPaperData = jsonpickle.decode(json_str)

            for author in paper_data.matched_authors:
                author_name = author.arxiv_name

                if author_name not in author_to_institutions:
                    author_to_institutions[author_name] = set()

                for affil in author.affiliations:
                    inst_id = affil.matched_ror.ror_id

                    # ---> THIS IS THE FIX <---
                    # Check if 'names' exists and has at least one item
                    if affil.matched_ror.names and len(affil.matched_ror.names) > 0:
                        inst_name = affil.matched_ror.names[0]  # Grab the first name
                    else:
                        inst_name = inst_id  # Fallback to ROR ID if list is empty

                    institution_names[inst_id] = inst_name

                    author_to_institutions[author_name].add(inst_id)

                    if inst_id not in institution_to_authors:
                        institution_to_authors[inst_id] = set()
                    institution_to_authors[inst_id].add(author_name)

        except Exception as e:
            print(f"Warning: Failed to parse a row: {e}")
            continue

    # Build connected dataclasses
    nodes: Dict[InstitutionID, InstitutionNode] = {}
    edges_dict: Dict[tuple, int] = {}
    shared_authors: List[SharedAuthor] = []

    # 1. Create Nodes
    for inst_id, authors in institution_to_authors.items():
        nodes[inst_id] = InstitutionNode(
            id=inst_id,
            name=institution_names.get(inst_id, inst_id),  # Fallback to ID if name isn't easily accessible
            author_count=len(authors)
        )

    # 2. Create Edges & Shared Authors
    for author_name, insts in author_to_institutions.items():
        inst_list = list(insts)

        # If an author belongs to more than 1 institution, they form a bridge
        if len(inst_list) > 1:
            shared_authors.append(
                SharedAuthor(id=author_name, name=author_name, institutions=inst_list)
            )

            # Create edges between all institutions this author belongs to
            for inst_a, inst_b in itertools.combinations(inst_list, 2):
                # Sort to ensure undirected consistency (A, B) is same as (B, A)
                edge_pair = tuple(sorted([inst_a, inst_b]))
                edges_dict[edge_pair] = edges_dict.get(edge_pair, 0) + 1

    # Format edges into the [ID, ID, weight] format
    edges: List[Edge] = [[pair[0], pair[1], float(weight)] for pair, weight in edges_dict.items()]

    graph_data = InstitutionGraph(
        nodes=nodes,
        edges=edges,
        shared_authors=shared_authors
    )

    print(
        f"Extraction complete: {len(nodes)} Institutions, {len(edges)} Collaborations, {len(shared_authors)} Shared Authors.")
    return graph_data


def build_networkx_from_struct(graph_data: InstitutionGraph) -> nx.Graph:
    """Converts the ConnectedPapers-style Dataclass into a NetworkX graph for analysis."""
    G = nx.Graph()

    for node_id, node_data in graph_data.nodes.items():
        G.add_node(node_id, author_count=node_data.author_count, name=node_data.name)

    for edge in graph_data.edges:
        G.add_edge(edge[0], edge[1], weight=edge[2])

    return G


# --- 3. ANALYSIS & VISUALIZATION ---

def analyze_network(G: nx.Graph):
    """Calculates Centrality and Louvain Communities for Institutions."""
    print("\n--- Running Network Analysis on Institutions ---")

    # 1. Degree Centrality
    degree_dict = dict(G.degree(weight='weight'))
    top_degree = sorted(degree_dict.items(), key=lambda x: x[1], reverse=True)[:10]

    print("\nTop 10 Most Collaborative Institutions:")
    for rank, (inst_id, degree) in enumerate(top_degree, 1):
        # ---> FIX: Look up the name stored inside the node attributes <---
        inst_name = G.nodes[inst_id].get('name', inst_id)
        print(f" {rank}. {inst_name} (Connections: {degree})")

    # 2. Community Detection
    print("\nDetecting Institutional Communities (Louvain Method)...")
    partition = community_louvain.best_partition(G, weight='weight')
    community_counts = Counter(partition.values())
    print(f"Found {len(community_counts)} distinct collaboration clusters.")

    return partition, degree_dict


def visualize_institutions(G: nx.Graph, partition: dict, degree_dict: dict):
    """Visualizes ONLY the most important hubs with maximum spacing."""
    print("\nGenerating Maximum Spaced Visualization for Top Hubs...")

    community_counts = Counter(partition.values())
    top_4_comms = [comm_id for comm_id, count in community_counts.most_common(4)]

    # 1. EVEN FEWER DOTS: Only the Top 8 most important institutions per cluster
    # (Max 32 dots total on the screen)
    top_nodes = []
    for comm_id in top_4_comms:
        comm_nodes = [n for n in G.nodes() if partition.get(n) == comm_id]
        comm_nodes_sorted = sorted(comm_nodes, key=lambda x: degree_dict[x], reverse=True)
        top_nodes.extend(comm_nodes_sorted[:8])

    SubG = G.subgraph(top_nodes)

    color_mapping = {
        top_4_comms[0]: "#1f77b4",
        top_4_comms[1]: "#ff7f0e",
        top_4_comms[2]: "#2ca02c",
        top_4_comms[3]: "#d62728",
    }
    colors = [color_mapping[partition[node]] for node in SubG.nodes()]

    # 2. SHRINK NODES: Slightly smaller circles make the gaps look much wider
    sizes = [min(G.nodes[node]['author_count'] * 15 + 100, 600) for node in SubG.nodes()]

    # 3. MAX SPACING: Bumped 'k' to 2.5 and iterations to 500 to force them far apart
    pos = nx.spring_layout(SubG, k=2.5, iterations=500, seed=42)

    internal_edges, bridge_edges = [], []
    for a, b in SubG.edges():
        if partition[a] == partition[b]:
            internal_edges.append((a, b))
        else:
            bridge_edges.append((a, b))

    # Huge canvas to accommodate the wide spacing
    fig, ax = plt.subplots(figsize=(20, 16))
    ax.set_title("Core Institutional Network (Top 8 Hubs - Maximum Spacing)",
                 fontsize=22, fontweight='bold', pad=20)

    # Draw black connections
    nx.draw_networkx_edges(SubG, pos, edgelist=internal_edges,
                           alpha=0.3, edge_color="black", width=0.8, ax=ax)
    nx.draw_networkx_edges(SubG, pos, edgelist=bridge_edges,
                           alpha=0.8, edge_color="black", width=2.0, ax=ax)

    # Draw nodes
    nx.draw_networkx_nodes(SubG, pos, node_color=colors, node_size=sizes,
                           alpha=0.9, edgecolors="black", linewidths=1.2, ax=ax)

    # Label ALL of these important hubs since there are so few
    labels = {n: G.nodes[n].get('name', n) for n in SubG.nodes()}

    # Offset labels heavily so they float well above the nodes
    label_pos = {k: (v[0], v[1] + 0.05) for k, v in pos.items()}

    nx.draw_networkx_labels(SubG, label_pos, labels=labels,
                            font_size=11, font_weight="bold", font_color="black",
                            bbox=dict(facecolor="white", edgecolor="black", alpha=0.9, pad=1.5, boxstyle="round,pad=0.3"),
                            ax=ax)

    legend_handles = [
        mpatches.Patch(color=color_mapping[top_4_comms[i]],
                       label=f"Cluster {i+1} Hubs")
        for i in range(len(top_4_comms))
    ]
    ax.legend(handles=legend_handles, loc='upper left',
              title="Legend", title_fontsize=14, fontsize=12, frameon=True)

    ax.axis("off")
    plt.tight_layout()
    plt.savefig("connected_institutions_network_max_spaced.png", dpi=300, bbox_inches='tight')
    print("Saved connected_institutions_network_max_spaced.png")
    plt.show()

def main():
    INPUT_FILE = "math_sample_processed_final.parquet"

    try:
        # 1. Build the ConnectedPapers-style data structure
        institution_struct = load_and_build_data_structures(INPUT_FILE)

        # 2. Convert to NetworkX for the heavy math
        G = build_networkx_from_struct(institution_struct)

        if G.number_of_nodes() == 0:
            print("The graph has no nodes! Please check your parquet file.")
            return

        # 3. Analyze and Visualize
        partition, degree_dict = analyze_network(G)
        visualize_institutions(G, partition, degree_dict)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()