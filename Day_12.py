# Problem link: https://leetcode.com/problems/largest-local-values-in-a-matrix/description
# Time: O(n^2)
# Space: O(1)
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        result = [[0] * (n - 2) for _ in range(n - 2)]

        for i in range(n - 2):
            for j in range(n - 2):
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        result[i][j] = max(result[i][j], grid[k][l])
                        
        return result
