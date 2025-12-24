import sys
import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        pq = [(0, src)]

        while pq:
            current_distance, current_vertex = heapq.heappop(pq)

            if current_distance > dist[current_vertex]:
                continue

            for u, v, w in self.graph:
                if u == current_vertex:
                    distance = current_distance + w
                    if distance < dist[v]:
                        dist[v] = distance
                        heapq.heappush(pq, (distance, v))

        return dist

    def bellman_ford(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0

        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != sys.maxsize and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        for u, v, w in self.graph:
            if dist[u] != sys.maxsize and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return None

        return dist

# Example usage
if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 3)
    g.add_edge(1, 2, 1)
    g.add_edge(1, 3, 2)
    g.add_edge(2, 1, 4)
    g.add_edge(2, 3, 8)
    g.add_edge(2, 4, 2)
    g.add_edge(3, 4, 7)
    g.add_edge(4, 3, 9)

    print("Dijkstra's shortest path from vertex 0:")
    print(g.dijkstra(0))

    print("Bellman-Ford shortest path from vertex 0:")
    print(g.bellman_ford(0))