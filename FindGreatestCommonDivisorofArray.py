#1979. Find Greatest Common Divisor of Array
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        return math.gcd(nums[0], nums[-1])
