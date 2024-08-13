#77. Combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def helper(start, path):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(start, n + 1):
                path.append(i)
                helper(i + 1, path)
                path.pop()
        helper(1, [])
        return res
