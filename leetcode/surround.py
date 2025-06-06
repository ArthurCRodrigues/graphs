"""
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

"""
from collections import deque
class Solution(object):
    def bfs(self,board,start,rows,cols,visited):
        #print("Starting new BFS.....")
        queue = []
        queue.append(start)
        index = 0
        error = False
        while queue[index:]:
            elem = queue[index]
            index += 1
            r,c = elem[0],elem[1]
            #print_sigle_element(board,elem)
            if (r == 0 or c == 0 or r == (rows-1) or c == (cols-1)):
                visited[r][c] = True
                error = True
            if board[r][c] == 'O' and not visited[r][c]:
                visited[r][c] = True
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    if board[nr][nc] == "O":
                        #print("\tChecked for ")
                        queue.append((nr,nc))
        if error == True: 
            return False
        else:
            for r,c in queue:
                board[r][c] = "X"
            return True
                


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
        return visited




if __name__ == "__main__":
    board = [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","O","O","X"],
        ["O","X","X","X"]
        ]
 
    for i in range(len(board)):
        print(board[i])
    
    sol = Solution()
    vsited = sol.solve(board)
    print("\n")
    for i in range(len(board)):
        print(board[i])
    