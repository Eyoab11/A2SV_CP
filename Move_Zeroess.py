# 283. Move Zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        non_zero = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[i], nums[non_zero] = nums[non_zero], nums[i]
                non_zero += 1
            i += 1
        return nums
