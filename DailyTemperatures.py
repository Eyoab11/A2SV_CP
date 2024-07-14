#739. Daily Temperatures
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        prefix = [0] * n
        i = 0
        while i < n:
            while stack and temperatures[i] > stack[-1] [0]:
                poppedT, poppedIdx = stack.pop()
                prefix[poppedIdx] = i - poppedIdx    
            stack.append((temperatures[i], i))
            i += 1
        return prefix
