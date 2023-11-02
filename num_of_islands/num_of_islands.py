from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != "1":
                return
            grid[r][c] = "0"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        ROWS = len(grid)
        COLS = len(grid[0])
        numOfIslands = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    numOfIslands += 1
                    dfs(row, col)
        return numOfIslands


    def test(self):
        print(self.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))
if __name__ == '__main__':
    Solution().test()