from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

    def bfs(self, start_node):
        visited = set()
        queue = deque([start_node])

        while queue:
            node = queue.popleft()
            if node not in visited:
                print(node)
                visited.add(node)
                queue.extend(neighbor for neighbor in self.graph.get(node, []) if neighbor not in visited)

# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', ['B', 'C'])
    g.add_edge('B', ['A', 'D', 'E'])
    g.add_edge('C', ['A', 'F'])
    g.add_edge('D', ['B'])
    g.add_edge('E', ['B', 'F'])
    g.add_edge('F', ['C', 'E'])

    print("Breadth-First Search starting from node 'A':")
    g.bfs('A')
