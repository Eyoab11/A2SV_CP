#2540. Minimum Common Value
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        first = 0
        second = 0
        res = []
        nums1.sort()
        nums2.sort()
        
        while first < len(nums1) and second < len(nums2):
            if nums1[first] == nums2[second]:
                res.append(nums1[first])
                break
            elif nums1[first] < nums2[second]:
                first += 1
            else:
                second += 1
        if len(res) == 0:
            return -1
        else:
            return res[0]
                
