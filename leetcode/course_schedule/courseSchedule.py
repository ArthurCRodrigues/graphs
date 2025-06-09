
class Solution(object):
    
    def to_adj(self,pr):
        adj = {}
        nodes = set()
        for req in pr:
            nodes.add(req[0])
            nodes.add(req[1])
        for node in nodes:
            edges = []
            for req in pr:
                if req[1] == node:
                    edges.append(req[0])
            adj[node] = edges
        return adj
    
    def has_path(self,start,table):
        stack = []
        visited = set()
        stack.append(start)
        first = True
        while stack:
            print(stack)
            elem = stack.pop()
            if elem not in visited:
                visited.add(elem)
                print(f"Current element -> {elem}")
                for neighbor in table[elem]:
                    print(f"{neighbor} is neighbor of {elem}")
                    stack.append(neighbor)
            elif elem == start and not first:
                print(f"{elem} == {start}...")
                return False
            first = False
            
        return True
    
    def canFinish(self,numCourses,prerequisites):
        if numCourses == 1 or prerequisites == []:
            return True
        for req in prerequisites:
            if req[::-1] in prerequisites:
                return False
        adj_list = self.to_adj(prerequisites)
        for node in adj_list.keys():
            if not self.has_path(node,adj_list):
                return False
        return True

if __name__ == '__main__':
    numCourses = 3
    prerequisites_list = [
                        [[1,0]],
                        [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]],
                        [[1,0],[0,2],[2,1]],
                        [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]],
                        [[1,0],[2,1],[3,2],[1,3]]
                          ]
    
    sol = Solution()
    for prerequisites in prerequisites_list:
        adj_list = sol.to_adj(prerequisites)
        print(adj_list)
        print("\t",sol.canFinish(numCourses,prerequisites))
        print("\n"*5)
    
