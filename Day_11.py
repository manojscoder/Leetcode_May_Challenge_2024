# Problem link: https://leetcode.com/problems/minimum-cost-to-hire-k-workers/description
# Time: O(nlogn + nlogk)
# Space: O(n)
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        ratio = []
        res = inf

        for i in range(len(quality)):
            ratio.append((wage[i] / quality[i], quality[i]))
        
        ratio.sort()

        maxHeap = []
        total_quality = 0

        for rate, quality in ratio:
            heapq.heappush(maxHeap, -quality)
            total_quality += quality

            if len(maxHeap) > k :
                total_quality += heapq.heappop(maxHeap)
            
            if len(maxHeap) == k:
                res = min(res, rate * total_quality)

        return res
