#Pancake Sorting
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        n = len(arr)
        for target in range(n, 1, -1):
            index_ = arr.index(target)
            if index_ != target - 1:
                if index_ != 0:
                    arr[:index_ + 1] = reversed(arr[:index_ + 1])
                    flips.append(index_ + 1)
                arr[:target] = reversed(arr[:target])
                flips.append(target)
        return flips
