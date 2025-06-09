
# Definition for a Node.
from collections import deque
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
    def add_neighbor(self,neighbor):
        self.neighbors.append(neighbor)
    def bfs(self,node):
        queue = deque()
        visited = set()
        queue.append(self)
        while queue:
            elem = queue.popleft()
            if elem not in visited:
                print("Current node -> ",elem.val)
                visited.add(elem)
                for neighbor in elem.neighbors: 
                    if neighbor not in visited:
                        queue.append(neighbor)

    def toAdj(self):
        queue = deque()
        visited = {}
        queue.append(self)
        while queue:
            elem = queue.popleft()
            if elem.val not in visited:
                print("Current node -> ",elem.val)
                visited[elem.val] = elem
                for neighbor in elem.neighbors: 
                    if neighbor.val not in visited:
                        queue.append(neighbor)
        #adj = [[] for i in range(len(visited))]
        adj = [node for node in visited.values()]
        #for k in visited:
            #print('K is ',k)
            #for n in visited[k].neighbors:
                #adj[k-1].append(n.val)
        return adj
    
    def clone(self):
        
            
        
    def __str__(self):
        return self.value

class Solution(object):

    def create_graph(self,adj_list):
        first_node = Node(val = 1)
        nodes = {1:first_node}
        for i in range(0,len(adj_list)):
            if i+1 not in nodes.keys():
                nodes[i+1] = Node(val=i+1)
            for neighbor in adj_list[i]:
                if neighbor not in nodes.keys():
                    nodes[neighbor] = Node(val=neighbor)
                nodes[i+1].add_neighbor(nodes[neighbor])
        
        return first_node
        
                

    def cloneGraph(self, node):
        if node == None:
            return []
        if node.neighbors == None:
            return [[]]
        return node.toAdj()


if __name__ == "__main__":
    adjList = [[2,4],[1,3],[2,4],[1,3]]
    #adjList = []
    sol = Solution()
    root = sol.create_graph(adjList)
    print(root.toAdj())
        