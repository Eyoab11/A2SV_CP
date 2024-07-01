#1493. Longest Subarray of 1's After Deleting One Element
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros = 0
        left = 0 
        res = 0

        for i in range(len(nums)):
            zeros += 1 if nums[i] == 0 else 0
            while zeros > 1:
                zeros -= 1 if nums[left] == 0 else 0
                left += 1
            cur = i - left
            res = max(res, cur)
        return res
