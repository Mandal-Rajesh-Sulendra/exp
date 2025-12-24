from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        traversal = []

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                traversal.append(vertex)
                queue.extend(neighbor for neighbor in self.graph.get(vertex, []) if neighbor not in visited)

        return traversal

    def dfs(self, start):
        visited = set()
        traversal = []

        def dfs_helper(vertex):
            visited.add(vertex)
            traversal.append(vertex)
            for neighbor in self.graph.get(vertex, []):
                if neighbor not in visited:
                    dfs_helper(neighbor)

        dfs_helper(start)
        return traversal

# Example usage:
if __name__ == "__main__":
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 5)

    print("BFS Traversal:", g.bfs(1))
    print("DFS Traversal:", g.dfs(1))