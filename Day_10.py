# Problem link: https://leetcode.com/problems/k-th-smallest-prime-fraction/description/
# Time: O(n^2)
# Space: O(n) for sorting
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        store = []

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                store.append((arr[i] / arr[j], [i, j]))
        
        store.sort(key = lambda x : x[0])
        return [arr[store[k - 1][1][0]], arr[store[k - 1][1][1]]]
