from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, src, dest):
        if src not in self.adj_list:
            self.add_vertex(src)
        if dest not in self.adj_list:
            self.add_vertex(dest)
        self.adj_list[src].append(dest)
        # For undirected graph, also add the reverse edge:
        # self.adj_list[dest].append(src)

    def display(self):
        for vertex in self.adj_list:
            print(f"{vertex}: {self.adj_list[vertex]}")
    
    def display_adj(self):
        print(self.adj_list)

    def traverse(self, start, method="DFS"):
        if method.upper() == "DFS":
            container = [start]
            pop_fn = lambda c: c.pop()
        elif method.upper() == "BFS":
            container = deque([start])
            pop_fn = lambda c: c.popleft()
        else:
            raise ValueError("Unknown traversal method: choose 'DFS' or 'BFS'")

        visited = set()
        while container:
            vertex = pop_fn(container)
            if vertex not in visited:
                print(vertex, end=' ')
                visited.add(vertex)
                for neighbor in self.adj_list.get(vertex, []):
                    if neighbor not in visited:
                        container.append(neighbor)

          

# Example usage:
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'D')
    g.traverse('A', method='DFS')
    print()  # New line after traversal
    g.traverse('A', method='BFS')