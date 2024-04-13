#88. Merge Sorted Array
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        last1 = m - 1
        last2 = n - 1
        summ = m + n - 1
        while last1 >= 0 and last2 >= 0:
            if nums1[last1] > nums2[last2]:
                nums1[summ] = nums1[last1]
                last1 -= 1
            else:
                nums1[summ] = nums2[last2]
                last2 -= 1
            summ -= 1
        nums1[:last2 + 1] = nums2[:last2 + 1]
