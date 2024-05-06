# Problem link: https://leetcode.com/problems/reverse-prefix-of-word/
# Time: O(n)
# Space: O(1)

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)):
            if word[i] == ch:
                return word[:i + 1][::-1] + word[i + 1:]
        return word
