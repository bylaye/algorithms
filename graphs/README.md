```
Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import topology
>>> import traversal
>>> graph = topology.UNDIRECTED_UNWEIGHT_GRAPH
>>> start = 'B' # start traversal with node B
>>> traversal.bfs(graph, start)
['B', 'A', 'E', 'C', 'D', 'F', 'G', 'H']
>>> traversal.dfs(graph, start)
['B', 'A', 'C', 'D', 'E', 'F', 'H', 'G']
>>> 
```
