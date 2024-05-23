# Problem link: https://leetcode.com/problems/the-number-of-beautiful-subsets/description
# Time: O(2 ^ n)
# Space: O(2 ^ n)
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        
        def dfs(i, count):
            if i == len(nums):
                return 1
            res = dfs(i + 1, count)
            if not count[nums[i] + k] and not count[nums[i] - k]:
                count[nums[i]] += 1
                res += dfs(i + 1, count)
                count[nums[i]] -= 1
            return res
            
        return dfs(0, defaultdict(int)) - 1
