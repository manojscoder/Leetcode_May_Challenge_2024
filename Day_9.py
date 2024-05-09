# Problem link: https://leetcode.com/problems/maximize-happiness-of-selected-children/description
# Time: O(nlogn)
# Space: O(n) for sorting
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        count = result = 0

        while k > 0:
            if happiness[count] - count > 0:
                result += (happiness[count] - count)
            else:
                return result
            count, k = count + 1, k - 1
        
        return result
