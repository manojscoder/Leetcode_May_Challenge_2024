# Problem link: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/description/
# Time: O(n)
# Space: O(1)
class Solution:
    def numSteps(self, s: str) -> int:
        num = steps = 0

        for i in range(len(s)):
            num += 2 ** (len(s) - i - 1) if s[i] == '1' else 0
        
        while num != 1:
            num, steps = num // 2 if num % 2 == 0 else num + 1, steps + 1
        
        return steps
