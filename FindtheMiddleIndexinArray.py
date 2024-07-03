#1991. Find the Middle Index in Array
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums) + 1
        p_sum = [0] * n
        for i in range(n - 1):
            p_sum[i + 1] = p_sum[i] + nums[i]
        for j in range(1, len(p_sum)):
            before = p_sum[j - 1]  
            after = p_sum[-1] - p_sum[j]  
            if before == after:
                return j - 1  
        return -1  
