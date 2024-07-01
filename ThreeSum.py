#15. 3Sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            if i > 0 and  a == nums[i-1]:
                continue 
            else:
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    if a + nums[left] + nums[right] == 0:
                        res.append([a, nums[left], nums[right]])
                        left += 1
                        while nums[left] == nums[left - 1] and left < right:
                            left += 1
                    elif a + nums[left] + nums[right] > 0:
                        right -= 1
                    else:
                        left += 1
        return res
            
                
