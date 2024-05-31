# Problem link: https://leetcode.com/problems/single-number-iii/description/
# Time: O(n)
# Space: O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor, mask, a, b = 0, 1, 0, 0

        for n in nums:
            xor ^= n

        while xor & mask == 0:
            mask <<= 1

        for n in nums:
            if mask & n:
                a ^= n
            else:
                b ^= n
        
        return [a, b]
