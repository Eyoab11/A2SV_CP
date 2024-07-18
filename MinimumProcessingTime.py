#2895. Minimum Processing Time
class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse= True)
        idx = 0
        ans = 0

        for i in processorTime:
            curMax = 0
            count = 0

            while idx < len(tasks) and count < 4:
                curMax = max(curMax, i + tasks[idx])
                idx += 1
                count += 1
            ans = max(ans, curMax)
        return ans
        
