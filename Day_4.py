# Problem link: https://leetcode.com/problems/boats-to-save-people/description/
# Time: O(nlogn)
# Space: O(n), for sorting
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse = True)
        result = left = 0
        right = len(people) - 1

        while left <= right:
            if people[left] + people[right] <= limit:
                right -= 1
            left += 1
            result += 1
        return result
            
