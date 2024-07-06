#1011. Capacity To Ship Packages Within D Days
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        res = right
        def helper(mid):
            count = 1
            cur = mid
            for i in weights:
                if cur - i < 0:
                    count += 1
                    cur = mid
                cur = cur - i
            return count <= days

        while left <= right:
            mid = (left + right) //2
            if helper(mid):
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return res
