#16. 3Sum Closest
class Solution:
    def threeSumClosest(self, nums: List[int], num: int) -> int:
        nums.sort() 
        res = float('inf') 
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                cur = nums[i] + nums[left] + nums[right] 
                if abs(cur - num) < abs(res - num):
                    res = cur
                if cur < num:
                    left += 1
                elif cur > num:
                    right -= 1
                else:
                    return num
        return res
