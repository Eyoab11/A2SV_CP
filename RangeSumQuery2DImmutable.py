#304. Range Sum Query 2D - Immutable
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.p_sum = [ [0]* (cols + 1) for i in range(rows+1)]
        for i in range(rows):
            p = 0
            for j in range(cols):
                p += matrix[i][j]
                up = self.p_sum[i][j+1]
                self.p_sum[i+1][j+1] = p + up

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        right = self.p_sum [row2+1] [col2+1]
        topLeft  =  self.p_sum [row1] [col1]
        left = self.p_sum [row2+1] [col1]
        up = self.p_sum [row1] [col2+1]
        return right - up -left + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
