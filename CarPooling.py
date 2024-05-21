# 1094. Car Pooling
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pas = [0] * 1001
        for numPas, initial, final in trips:
            pas[initial] += numPas
            pas[final] -= numPas
        max_ = 0
        for numPas in pas:
            max_ += numPas
            if max_ > capacity:
                return False
        return True
