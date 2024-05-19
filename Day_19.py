# Problem link: https://leetcode.com/problems/find-the-maximum-sum-of-node-values/description
# Time: O(nlogn)
# Space: O(n)
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        store = sorted([(n ^ k) - n for n in nums], reverse = True)
        res = sum(nums)

        for i in range(0, len(nums) - 1, 2):
            total = store[i] + store[i + 1]
            if total <= 0:
                break
            res += total
        
        return res
