#424. Longest Repeating Character Replacement
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = {}
        left = 0
        length = 0
        count = 0
        for i,n in enumerate(s):
            res[n] = res.get(n, 0) + 1
            count = max(count, res[n])
            while (i - left + 1 - count) > k:
                res[s[left]] -= 1
                left += 1
            length = max(length, i - left + 1)
        return length
