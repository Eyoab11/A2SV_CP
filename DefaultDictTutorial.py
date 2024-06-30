#DefaultDict Tutorial
# Enter your code here. Read input from STDIN. Print res to STDOUT
from collections import defaultdict
import sys
input = sys.stdin.read
nums = input().splitlines()
n, m = map(int, nums[0].split())
d = defaultdict(list)
for i in range(1, n + 1):
    word = nums[i]
    d[word].append(i)
res = []
for j in range(n + 1, n + 1 + m):
    word = nums[j]
    if word in d:
        res.append(" ".join(map(str, d[word])))
    else:
        res.append("-1")
print("\n".join(res))
