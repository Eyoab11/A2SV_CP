#334. Increasing Triplet Subsequence
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        left = float('inf')
        right = float('inf')
        i = 0
        while i < len(nums):
            temp = nums[i]
            if temp <= left:
                left = temp
            elif temp <= right:
                right = temp
            else:
                return True
            i += 1
        return False

