#1248. Count Number of Nice Subarrays
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        n = len(nums)
        count = 0
        pSum = [0] * (n + 1)
        pSum[0] = 1
        for i in range(n):
            if nums[i] % 2 != 0:
                count += 1
            if count >= k:
                res += pSum[count - k]      
            pSum[count] += 1
        return res
