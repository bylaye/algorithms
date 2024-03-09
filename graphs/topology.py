"""
Topology Graph define relation beetwen nodes with edges
"""

UNDIRECTED_UNWEIGHT_GRAPH = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E'],
    'C': ['A', 'D', 'H'],
    'D': ['A', 'C', 'E', 'H'],
    'E': ['B', 'D', 'F', 'G'],
    'F': ['E', 'H', 'G'],
    'H': ['C', 'D', 'F'],
    'G': ['E', 'F']
}