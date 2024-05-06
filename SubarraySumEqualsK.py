#560. Subarray Sum Equals K
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curSum = 0
        mp = {0:1}
        ans = 0
        for num in nums:
            curSum += num
            x  = curSum - k
            if x in mp:
                ans += mp[x]
            mp[curSum] = mp.get(curSum,0) + 1
        return ans
