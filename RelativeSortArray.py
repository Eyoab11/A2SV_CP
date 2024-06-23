#1122. Relative Sort Array
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr2[i] == arr1[j]:
                    res.append(arr1[j])
        res2 = []
        for i in arr1:
            if i not in res:
                res2.append(i)
        res2.sort()
        for i in res2:
            res.append(i)
        return res
