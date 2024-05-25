# Problem link: https://leetcode.com/problems/word-break-ii/description
# Time: O(2 ^ n)
# Space: O(n), for cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words, cache = set(wordDict), {}

        def backtrack(i):
            if i == len(s):
                return [""]
            elif i in cache:
                return cache[i]
            res = []

            for j in range(i, len(s)):
                w = s[i : j + 1]

                
                if w not in words:
                    continue

                strings = backtrack(j + 1)

                if not strings:
                    continue

                for sub in strings:
                    word = w
                    if sub:
                        word += " " + sub
                    res.append(word)

            cache[i] = res
            return res

        return backtrack(0)
