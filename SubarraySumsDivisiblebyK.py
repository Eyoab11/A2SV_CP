#974. Subarray Sums Divisible by K
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        p_sum = [0] * k
        num = 0
        for i in nums:
            num += i % k
            p_sum[num % k] += 1
        res = p_sum[0]
        for c in p_sum:
            res += (c * (c - 1)) // 2
        return res
