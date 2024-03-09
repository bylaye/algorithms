from typing import *

"""
Breadth For Search algorithm traversal graph 
with input DS dictionary
input : {'A':['B', 'C'], 'B':['A', 'C'], 'C':['A', 'B']}, start='A'
return ['A', 'B', 'C']
"""
def bfs(graph:{str:List[str]}, start:str) -> List[str]: # type: ignore
    visited = [start]
    queue = [start]
    while queue:
        node = queue.pop(0)
        for vertex in graph[node]:
            if vertex not in visited:
                visited.append(vertex)
                queue.append(vertex)
    return visited


"""
Depth For Search algorithm traversal graph 
with input DS dictionary
input : {'A':['B', 'C'], 'B':['A', 'C'], 'C':['A', 'B']}, start='A'
return ['A', 'B', 'C']
"""
def dfs(graph:{str:List[str]}, start:str) -> List[str]: # type: ignore
    visited = [start]
    def depth(node):
        for vertex in graph[node]:
            if vertex not in visited:
                visited.append(vertex)
                depth(vertex)
    depth(start)
    return visited
