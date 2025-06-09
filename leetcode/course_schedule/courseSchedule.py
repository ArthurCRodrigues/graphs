from collections import deque
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
        queue = deque()
        visited = set()
        queue.append(start)
        first = True
        while queue:
            print(queue)
            elem = queue.popleft()
            if elem not in visited:
                visited.add(elem)
                print(f"Current element -> {elem}")
                for neighbor in table[elem]:
                    print(f"{neighbor} is neighbor of {elem}")
                    queue.append(neighbor)
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
        return self.has_path(prerequisites[0][1],self.to_adj(prerequisites))

if __name__ == '__main__':
    numCourses = 3
    prerequisites_list = [
                        [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]],
                        [[1,0],[0,2],[2,1]],
                        [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]],
                        [[1,0],[2,1],[3,2],[1,3]]
                          ]
    

    sol = Solution()
    for prerequisites in prerequisites_list:
        print(sol.to_adj(prerequisites))
        print("\t",sol.canFinish(numCourses,prerequisites))
        print("\n"*5)
    
