#2165. Smallest Value of the Rearranged Number
class Solution:
    def smallestNumber(self, num: int) -> int:
        if num >= 0:
            x = list(str(num))
            x.sort()
            if x[0] == '0':
                for i in range(len(x)):
                    if x[i] != '0':
                        x[0], x[i] = x[i], x[0]
                        break
            res = ''.join(x)
        else:
            x = list(str(abs(num)))
            x.sort(reverse=True)
            res = '-' + ''.join(x)
        
        return int(res)
