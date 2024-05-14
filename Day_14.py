# Problem link: https://leetcode.com/problems/path-with-maximum-gold/description
# Time: O(m * n)
# Space: O(m *n), for recursive call stack
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        result, visit, rows, cols = 0, set(), len(grid), len(grid[0])

        def backtrack(r, c, gold):
            nonlocal result
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0 or (r, c) in visit:
                return

            num = grid[r][c]
            grid[r][c] = 0
            result = max(result, gold + num)

            backtrack(r - 1, c, gold + num)
            backtrack(r + 1, c, gold + num)
            backtrack(r, c - 1, gold + num)
            backtrack(r, c + 1, gold + num)

            grid[r][c] = num

        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 0:
                    backtrack(i, j, 0)
        
        return result
