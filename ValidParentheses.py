# 20. Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(': ')', '{': '}', '[': ']'}
        for char in s:
            if char in pairs:
                stack.append(char)
            elif not stack or pairs[stack.pop()] != char:
                return False
        return not stack
