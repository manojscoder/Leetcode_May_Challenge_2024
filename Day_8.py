# Problem link: https://leetcode.com/problems/relative-ranks/description
# Time: O(nlogn)
# Space: O(n)
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        result = [0] * len(score)
        store = {val : idx for idx, val in enumerate(score)}
        
        score.sort(reverse = True)

        for i in range(len(score)):
            if i < 3:
                if i == 0:
                    result[store[score[i]]] = "Gold Medal"
                elif i == 1:
                    result[store[score[i]]] = "Silver Medal"
                else:
                    result[store[score[i]]] = "Bronze Medal"
            else:
                result[store[score[i]]] = str(i + 1)
        
        return result
