# Problem link: https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/description/
# Time: O(n)
# Space: O(n)
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        result, n = 0, len(arr)

        prev_xor_cnt = {0 : 1}
        prev_xor_sum = defaultdict(int)
        prefix = 0

        for i in range(n):
            prefix ^= arr[i]

            if prefix in prev_xor_cnt:
                result += i * prev_xor_cnt[prefix] - prev_xor_sum[prefix]
            
            if prefix not in prev_xor_cnt:
                prev_xor_cnt[prefix] = 0
            
            prev_xor_cnt[prefix] += 1
            prev_xor_sum[prefix] += i + 1
        
        return result

