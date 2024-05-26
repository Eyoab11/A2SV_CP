#C. Less or Equal
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
if k == 0:
    if a[0] == 1:
        print("-1")
    else:
        print("1")
else:
    if n == 1:
        print(a[0])
    elif n == k:
        print(a[k - 1])
    else:
        k -= 1
        if k + 1 < n and a[k] != a[k + 1]:
            print(a[k])
        else:
            print("-1")
