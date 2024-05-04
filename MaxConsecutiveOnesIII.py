#1004. Max Consecutive Ones III
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        max_ = 0
        i = 0
        while i < len(nums):
            n = nums[i]
            k -= (1 - n)
            if k < 0:
                k += (1 - nums[left])
                left += 1
            max_ = max(max_, i - left + 1)
            i += 1
        return max_
