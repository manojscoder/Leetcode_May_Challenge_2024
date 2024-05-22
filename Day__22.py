# Problem link: https://leetcode.com/problems/palindrome-partitioning
# Time: O(n * 2 ^ n)
# Space: O(n * 2 ^ n) for recursive stack
class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        part = []
        self.dfs(s, res, part, 0)
        return res

    def dfs(self, s: str, res: list[list[str]], part: list[str], idx: int):
        if idx >= len(s):
            res.append(part.copy())
            return
        
        for i in range(idx, len(s)):
            if self.palindrome(s, idx, i):
                part.append(s[idx:i + 1])
                self.dfs(s, res, part, i + 1)
                part.pop()

    def palindrome(self, s: str, i: int, j: int) -> bool:
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
