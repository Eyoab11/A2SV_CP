#150. Evaluate Reverse Polish Notation
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        lists= ["+", "-", "*", "/"]
        for i in tokens:
            if i not in lists:
                stack.append(int(i))
            else:  
                left = stack.pop()
                right = stack.pop()
                if i == "+":
                    res = right + left
                elif i == "-":
                    res = right - left
                elif i == "*":
                    res = right * left
                elif i == "/":
                    res = int(right / left)
                stack.append(res)
        return stack[0]


