# Problem link: https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/description/
# Time: O(n)
# Space: O(n)
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        count = [0] * (len(nums) + 1)
        for i in nums:
            count[min(i, len(nums))] += 1
        
        total = 0
        for i in range(len(nums), -1 ,-1):
            total += count[i]
            if i == total:
                return total
                
        return -1
