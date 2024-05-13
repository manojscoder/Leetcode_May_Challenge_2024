# Problem link: https://leetcode.com/problems/score-after-flipping-matrix/description
# Time: O(m * n)
# Space: O(1)
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        result = rows * (2 ** (cols - 1))

        for i in range(1, cols):
            count = 0
            for j in range(rows):
                if grid[j][0] != grid[j][i]:
                    count += 1
    
            result += (max(count, rows - count) * (2 ** (cols - i - 1)))
           
        return result
