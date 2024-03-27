#1309. Decrypt String from Alphabet to Integer Mapping
class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = ""
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                number = int(s[i - 2:i])
                result += chr(number + ord('a') - 1)
                i -= 3
            else:
                number = int(s[i])
                result += chr(number + ord('a') - 1)
                i -= 1
        return result[::-1]
        
        
