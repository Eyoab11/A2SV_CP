#125. Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = []
        for i in range(len(s)):
            if s[i].isalnum():
                word.append(s[i].lower())
        left = 0
        right = len(word) - 1
        while left < right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
        
        return True
