#394. Decode String
class Solution:
    def decodeString(self, s: str) -> str:
        res = []
        for i in range(len(s)):
            if s[i] != ']':
                res.append(s[i])
            else:
                encoded = ''
                while res[-1] != '[':
                    encoded = res.pop() + encoded
                res.pop()
                k = ''
                while res and res[-1].isdigit():
                    k = res.pop() + k
                res.append(int(k) * encoded)
        return "".join(res)
