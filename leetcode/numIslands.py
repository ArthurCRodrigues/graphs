from collections import deque
class Solution(object):
    def neighbors(self,grid, node):
        
        neighbors = []

        directions = []
        directions.append([1,0]) #up
        directions.append([-1,0]) #down
        directions.append([0,1]) #right
        directions.append([0,-1]) #left
        for direction in directions:
            next_pos = (node[0]+direction[0],node[1]+direction[1])
            if next_pos[0] in range(0,len(grid)) and \
            next_pos[1] in range(0,len(grid[0])) and \
            grid[next_pos[0]][next_pos[1]] == "1":
                neighbors.append(next_pos)
        return neighbors





    def bfs(self,start : set, visited : list, grid):
        
        queue = deque()
        queue.append(start)
        while queue:
            elem = queue.popleft()
            if not visited[elem[0]][elem[1]]:
                visited[elem[0]][elem[1]] = True
                #print(f"Visited -> {visited}")
                for neighbor in neighbors(grid,elem):
                    if not visited[neighbor[0]][neighbor[1]]:
                        queue.append(neighbor)
        return 1
                




    def numIslands(self,grid):
        islands = 0
        visited = []
        for i in range(len(grid)):
            col = []
            for i in range(len(grid[0])):
                col.append(False)
            visited.append(col)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and not visited[i][j]: #a node id is its position, since all values are either 1 or 0
                    islands += bfs((i,j),visited,grid)
                    
        return islands
                    

        





if __name__ == "__main__": 
    grid = [
    ["1","0","1","1"]

    ]
    print(Solution.numIslands(grid))
