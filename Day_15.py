# Problem link: https://leetcode.com/problems/find-the-safest-path-in-a-grid/description
# Time: O(n ^ 2 * log n)
# Space: O(n ^ 2)
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        N = len(grid)
        
        def in_bound(r, c):
            return min(r, c) >= 0 and max(r, c) < N

        def count_distance():
            q = deque()
            min_dist = {}
            for i in range(N):
                for j in range(N):
                    if grid[i][j] == 1:
                        q.append((i, j, 0))
                        min_dist[(i, j)] = 0
            
            while q:
                row, col, dist = q.popleft()
                lst = [[row + 1, col], [row - 1, col], [row, col - 1], [row, col + 1]]

                for r, c in lst:
                    if in_bound(r, c) and (r, c) not in min_dist:
                        q.append((r, c, dist + 1))
                        min_dist[(r, c)] = dist + 1
            
            return min_dist
        
        min_dist, maxHeap, visit = count_distance(), [], set((0, 0))
        heapq.heappush(maxHeap, (-min_dist[(0, 0)], 0, 0))


        while maxHeap:
            dist, row, col = heapq.heappop(maxHeap)
            dist *= -1

            if row == N - 1 and col == N - 1:
                return dist

            lst = [[row + 1, col], [row - 1, col], [row, col - 1], [row, col + 1]]

            for r, c in lst:
                if in_bound(r, c) and (r, c) not in visit:
                    visit.add((r, c))
                    heapq.heappush(maxHeap, (-min(min_dist[(r, c)], dist), r, c))
