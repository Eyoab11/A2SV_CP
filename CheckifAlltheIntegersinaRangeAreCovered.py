#1893. Check if All the Integers in a Range Are Covered
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = [False] * 51  
        for i, j in ranges:
            for num in range(i, j + 1):
                if 1 <= num <= 50:
                    covered[num] = True
        for num in range(left, right + 1):
            if not covered[num]:
                return False
        return True
