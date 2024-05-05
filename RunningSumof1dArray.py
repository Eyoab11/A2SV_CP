#1480. Running Sum of 1d Array
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p_sum = [0] *( n+1 )
        for i in range(n):
            p_sum[i+1] = p_sum[i] + nums[i]
        p_sum.pop(0)
        return p_sum
