#69. Sqrt(x)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x  
        left = 0
        right = x
        while left < right:
            mid = left + (right - left ) // 2
            if mid **2 <= x:
                left = mid + 1
            else:
                right = mid
        return left-1
                
