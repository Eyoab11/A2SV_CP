#925. Long Pressed Name
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        res = 0
        count = 0
        n = len(name)
        
        while count < len(typed):
            if res < n and name[res] == typed[count]:
                res += 1
                count += 1
            elif count > 0 and typed[count] == typed[count - 1]:
                count += 1
            else:
                return False
        
        return res == n
