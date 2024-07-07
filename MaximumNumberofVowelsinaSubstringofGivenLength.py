#1456. Maximum Number of Vowels in a Substring of Given Length
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        count = 0
        left = 0
        res = 0
        for i in range(len(s)):
            if s[i] in vowels:
                count += 1
            if i - left + 1 > k:
                if s[left] in vowels:
                    count -= 1
                left += 1
            res = max(res, count)
        return res

        
        
        

        
