#Largest Number
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = list(map(str, nums))
        def compare(x, y):
            return int(y + x) - int(x + y)
        nums_str.sort(key=cmp_to_key(compare))
        res_str = ''.join(nums_str)
        if res_str[0] == '0':
            return '0'
        return res_str
