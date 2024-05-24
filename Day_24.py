# Problem link: https://leetcode.com/problems/maximum-score-words-formed-by-letters/description
# Time: O(2 ^ n * W + L), where W is maximum length of the word and L is length of letters
# Space: O(n)
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letter_cnt = Counter(letters)

        def helper(word):
            store = Counter(word)
            for c in word:
                if store[c] > letter_cnt[c]:
                    return False
            return True
        
        def get_score(word):
            res_score = 0
            for c in word:
                res_score += score[ord(c) - ord('a')]
            return res_score


        def dfs(i):
            if i == len(words):
                return 0
            
            res = dfs(i + 1)
            
            if helper(words[i]):
                for c in words[i]:
                    letter_cnt[c] -= 1
                res = max(res, get_score(words[i]) + dfs(i + 1))
                for c in words[i]:
                    letter_cnt[c] += 1
            
            return res
        
        return dfs(0)
