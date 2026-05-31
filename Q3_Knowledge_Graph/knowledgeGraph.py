import networkx as nx
import matplotlib.pyplot as plt


G = nx.DiGraph()


edges = [
    ("Student", "Mahindra University", "studies_at"),
    ("Student", "Python", "learns"),
    ("Student", "Artificial Intelligence", "studies"),

    ("Artificial Intelligence", "Machine Learning", "includes"),
    ("Artificial Intelligence", "Knowledge Graphs", "includes"),

    ("Machine Learning", "Deep Learning", "contains"),

    ("Knowledge Graphs", "Neo4j", "built_with"),
    ("Knowledge Graphs", "NetworkX", "built_with"),
    ("Knowledge Graphs", "RDF", "represented_by"),

    ("Python", "NetworkX", "supports"),
    ("Python", "Matplotlib", "supports"),

    ("NetworkX", "Graph Visualization", "used_for"),
    ("Matplotlib", "Graph Visualization", "used_for")
]

for source, target, relation in edges:
    G.add_edge(source, target, relation=relation)
plt.figure(figsize=(12, 8))

pos = nx.spring_layout(G, seed=42)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=2500,
    font_size=9,
    arrows=True
)

edge_labels = nx.get_edge_attributes(G, "relation")
nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels,
    font_size=7
)

plt.title("Knowledge Graph Example")
plt.axis("off")
plt.show()
