#2373. Largest Local Values in a Matrix
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        result = [[0] * (n - 2) for _ in range(n - 2)]
        
        for i in range(n - 2):
            for j in range(n - 2):
                max_matrix = 0
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        max_matrix = max(max_matrix, grid[k][l])
                
                result[i][j] = max_matrix
        
        return result
