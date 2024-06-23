#350. Intersection of Two Arrays II
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {}
        for num in nums1:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        print(count)
        res = []
        for num in nums2:
            if num in count and count[num] > 0:
                res.append(num)
                count[num] -= 1
        return res
