# 2381. Shifting Letters II
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0] * (len(s) +1)
        for left, right, pat in shifts:
            n = 1 if pat == 1 else -1
            prefix[left] += n
            prefix[right + 1] -= n
        res = ''
        for i in range(len(s)):
            if i != 0:
                prefix[i] += prefix[i -1]
            unicode_ = (ord(s[i]) - ord('a') + prefix[i]) % 26 + ord('a')
            res += chr(unicode_)
        return res
