# Problem link: https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/description/
# Time: O(n)
# Space: O(n)
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        store = set(nums)
        result = -1
        for i in nums:
            if i > 0 and -i in store:
                result = max(result, i)
        return result
