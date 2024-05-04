#3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_ = 0
        left = 0
        idx = {}
        for right in range(len(s)):
            if s[right] in idx and idx[s[right]] >= left:
                left = idx[s[right]] + 1
            idx[s[right]] = right
            max_ = max(max_, right - left + 1)
        return max_
