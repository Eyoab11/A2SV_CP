#209. Minimum Size Subarray Sum
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_ = float('inf')
        left=0
        window_sum=0
        for i in range(len(nums)):
            window_sum+=nums[i]
            while window_sum>=target:
                min_=min(min_,i-left+1)
                window_sum-=nums[left]
                left+=1
        return min_ if min_ != float('inf') else 0
