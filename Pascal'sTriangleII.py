#119. Pascal's Triangle II
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def helper(idx):
            if idx == 0:
                return [1]
            elif idx == 1:
                return [1, 1]
            else:
                prev = helper(idx - 1)
                row = [1] * (idx + 1)
                for i in range(1, idx):
                    row[i] = prev[i - 1] + prev[i]
                return row
        
        return helper(rowIndex)
