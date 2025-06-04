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
        self.adj_list[dest].append(src)

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


    def has_path_bfs(self,start,end):
        queue = [ start ]
        visited = set()
        while queue:
            node = queue.pop(0)
            print(node)
            if node == end:
                return True
            if node not in visited:
                visited.add(node)
                #print("Neighbors: ", self.adj_list[node])
                for neighbour in self.adj_list[node]:
                    if neighbour not in visited:
                        queue.append(neighbour)
        return False
    
    def shortest_path_bfs(self,start,end):
        queue = [[start]] #each element of the queue is a list that represents a path (the order of elements in that list is the traversal order of the path)
        visited = set()
        while queue:
            current_path = queue.pop(0)
            current_node = current_path[-1] #last node represents the end of the current path //aka the next node to check for neighbors
            print(current_node)
            if current_node == end:
                return current_path
            if current_node not in visited:
                visited.add(current_node)
                for neighbor in self.adj_list[current_node]:
                    if neighbor not in visited:
                        new_path = list(current_path)
                        new_path.append(neighbor)
                        queue.append(new_path)
        return None
class directedGraph(Graph):
    def add_edge(self, src, dest):
        if src not in self.adj_list:
            self.add_vertex(src)
        if dest not in self.adj_list:
            self.add_vertex(dest)
        self.adj_list[src].append(dest)

# Example usage:
if __name__ == "__main__":
    choice = int(input("Choose graph type:\n1) Directed Graph\n2) Undirected Graph\n>>"))
    if choice == 1:
        g = directedGraph()
        g.add_edge('A','B')
        g.add_edge('C','A')
        g.add_edge('B','D')
        g.add_edge('D','B')
        g.add_edge('D','E')
        g.add_edge('A','E')
        g.add_edge('C','E')
        g.display()
        print(g.has_path_bfs('A','E'))
        print(g.shortest_path_bfs('A','E'))
    elif choice == 2:
        g = Graph()
        g.add_edge('A','B')
        g.add_edge('A','C')
        g.add_edge('B','D')
        g.add_edge('D','E')
        g.add_edge('A','E')
        g.add_edge('C','E')
        g.display()