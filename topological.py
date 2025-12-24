from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()
    
    def add_edge(self, u, v):
        """Add a directed edge from u to v"""
        self.graph[u].append(v)
        self.vertices.add(u)
        self.vertices.add(v)
    
    def topological_sort_dfs(self):
        """Topological sort using DFS"""
        visited = set()
        stack = []
        
        def dfs(vertex):
            visited.add(vertex)
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    dfs(neighbor)
            stack.append(vertex)
        
        for vertex in self.vertices:
            if vertex not in visited:
                dfs(vertex)
        
        return stack[::-1]
    
    def topological_sort_kahn(self):
        """Topological sort using Kahn's algorithm (BFS)"""
        in_degree = {v: 0 for v in self.vertices}
        
        for u in self.graph:
            for v in self.graph[u]:
                in_degree[v] += 1
        
        queue = deque([v for v in self.vertices if in_degree[v] == 0])
        result = []
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            for neighbor in self.graph[vertex]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return result


# Example usage
if __name__ == "__main__":
    g = Graph()
    edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
    
    for u, v in edges:
        g.add_edge(u, v)
    
    print("DFS approach:", g.topological_sort_dfs())
    print("Kahn's approach:", g.topological_sort_kahn())