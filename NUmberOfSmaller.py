# codeforces B. Number of Smaller
n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
res = []
for i in arr2:
    left = 0
    right = n
    while left < right:
        mid = (left + right) // 2
        if arr1[mid] < i:
            left = mid + 1
        else:
            right = mid
    res.append(left)
print(*res)
