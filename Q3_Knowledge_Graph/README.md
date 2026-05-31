# Knowledge Graph Visualization Using NetworkX

## Overview

This demonstrates the creation and visualization of a Knowledge Graph using Python, NetworkX, and Matplotlib. The graph represents relationships between concepts in the field of Artificial Intelligence, including Machine Learning, Deep Learning, Knowledge Graphs, and the tools used to develop them.

---

## Objectives

- Understand the concept of Knowledge Graphs.
- Represent entities and their relationships using a graph structure.
- Visualize interconnected knowledge using Python.
- Explore graph-based data representation in Artificial Intelligence.

---

## Technologies Used

- Python 3
- NetworkX
- Matplotlib

---

## Graph Structure

The Knowledge Graph contains the following entities:

### Main Entities
- Student
- Mahindra University
- Python
- Artificial Intelligence
- Machine Learning
- Deep Learning
- Knowledge Graphs
- Neo4j
- NetworkX
- RDF
- Matplotlib
- Graph Visualization

### Relationships

| Source | Relationship | Target |
|----------|-------------|---------|
| Student | studies_at | Mahindra University |
| Student | learns | Python |
| Student | studies | Artificial Intelligence |
| Artificial Intelligence | includes | Machine Learning |
| Artificial Intelligence | includes | Knowledge Graphs |
| Machine Learning | contains | Deep Learning |
| Knowledge Graphs | built_with | Neo4j |
| Knowledge Graphs | built_with | NetworkX |
| Knowledge Graphs | represented_by | RDF |
| Python | supports | NetworkX |
| Python | supports | Matplotlib |
| NetworkX | used_for | Graph Visualization |
| Matplotlib | used_for | Graph Visualization |

---

## Working Principle

1. A directed graph is created using NetworkX.
2. Nodes represent entities or concepts.
3. Edges represent relationships between entities.
4. A spring layout algorithm positions nodes automatically.
5. NetworkX draws the graph structure.
6. Matplotlib displays the graph visually.
7. Edge labels indicate the type of relationship between connected nodes.

---

## Installation

Install the required libraries:

```bash
pip install networkx matplotlib
```

For Ubuntu/WSL:

```bash
python3 -m pip install networkx matplotlib --break-system-packages
```

---

## How to Run

1. Save the Python file.
2. Open Terminal or Command Prompt.
3. Navigate to the project directory.
4. Run the program:

```bash
python knowledge_graph.py
```

5. The graph visualization window will appear displaying the Knowledge Graph.
