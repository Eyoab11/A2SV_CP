#1509. Minimum Difference Between Largest and Smallest Value in Three Moves
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) < 5:
            return 0
        else:
            return min(nums[-1] - nums[3], nums[-2] - nums[2],nums[-3] - nums[1],nums[-4] - nums[0])
