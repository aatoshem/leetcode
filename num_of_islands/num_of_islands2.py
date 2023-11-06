# 200. Number of Islands [https://leetcode.com/problems/number-of-islands/description/]
import unittest
from typing import List
class Solution(unittest.TestCase):
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c) -> None:
            if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == "1":
                grid[r][c] = "0"
                moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
                for dr, dc in moves:
                    dfs(r + dr, c + dc)

        ROWS = len(grid)
        COLS = len(grid[0])
        numOfIslands = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    numOfIslands += 1
                    dfs(row, col)
        return numOfIslands

    def test_num_of_islands(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        self.assertEqual(self.numIslands(grid), 3)
