#Remove Smallest
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()  
    if n == 1:
        print("YES")
        continue
    left = []
    for i in range(1, n):
        difference = abs(a[i] - a[i-1])
        left.append(difference)
    left.sort(reverse=True) 
    if left[0] > 1:
        print("NO")
    else:
        print("YES")
