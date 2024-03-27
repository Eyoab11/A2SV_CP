#2460. Apply Operations to an Array
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        j = 0
        for i in range(n - 1):
            if nums[i] == nums[i + 1] and nums[i] != 0:
                nums[i] *= 2
                nums[i + 1] = 0
                i+=1
        
        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j+=1
         
        return nums
