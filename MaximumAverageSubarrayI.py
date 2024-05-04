#643. Maximum Average Subarray I
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k]) 
        max_average = window_sum / k
        left = 0
        right = k
        while right < len(nums):
            window_sum -= nums[left]
            window_sum += nums[right]
            max_average = max(max_average, window_sum / k)
            left += 1
            right += 1
        return max_average
