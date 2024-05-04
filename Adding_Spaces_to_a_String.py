#2109. Adding Spaces to a String
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = [''] * (len(s) + len(spaces))
        sp = 0  
        ss = 0  
        ans = 0  
        while sp < len(spaces) and ss < len(s):
            idx = spaces[sp]
            while ss < idx and ss < len(s):
                res[ans] = s[ss]
                ans += 1
                ss += 1
            res[ans] = ' '
            ans += 1
            sp += 1
        while ss < len(s):
            res[ans] = s[ss]
            ans += 1
            ss += 1
        return ''.join(res)
