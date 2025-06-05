"""
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

My Approach:
- Use recursion on BFS algo
- Recursive call for traversal
- If it manages detects a node on the edge, quit function
- If not, the recursive unstack will go filling the searched nodes with X
"""

class Solution(object):
    def bfs(self,board,node,rows,cols,visited):
        r,c = node[0],node[1]
        if (r == 0 or c == 0 or r == (rows-1) or c == (cols-1)) and board[r][c] == 'O':
            return
        if board[r][c] == "O" and not visited[r][c]:
            visited[r][c] = True
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for dr,dc in directions:
                self.bfs(board,(r+dr,c+dc),rows,cols,visited)
            board[r][c] = "X" # the method is breaking only when it finds a next node with the constraints. if there's a graph which the 3 nodes are not in the constraints but the final is, it won't break for the three ones
                
        

    def solve(self, board):
        rows,cols = len(board), len(board[0])
        visited = []
        for i in range(rows):
            col = []
            for j in range(cols):
                col.append(False)
            visited.append(col)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and not visited[i][j]:
                    self.bfs(board,(i,j),rows,cols,visited)






if __name__ == "__main__":
    board = [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","O","O","X"],
        ["X","O","O","X"]
        ]
 
    for i in range(len(board)):
        print(board[i])
    
    sol = Solution()
    sol.solve(board)
    print("\n")
    for i in range(len(board)):
        print(board[i])
    