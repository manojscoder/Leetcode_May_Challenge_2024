# Problem link: https://leetcode.com/problems/palindrome-partitioning
# Time: O(2 ^ n)
# Space: O(2 ^ n) for recursive stack
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def dfs(idx, p):
            if idx == len(s):
                result.append(p.copy())
                return
            
            for i in range(idx, len(s)):
                if s[idx : i + 1] == s[idx : i + 1][::-1]:
                    p.append(s[idx : i  + 1])
                    dfs(i + 1, p)
                    p.pop()
        
        dfs(0, [])
        return result
