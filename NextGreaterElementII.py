# 503. Next Greater Element II
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []
        
        for i in range(2 * n):  
            cur = nums[i % n]
            while stack and cur > nums[stack[-1]]:
                index = stack.pop()
                res[index] = cur
            if i < n:
                stack.append(i % n)
        
        return res
