# Container With Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_ = 0 
        n = len(height)
        left = 0
        right = n - 1
        
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_ = max(max_, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_
