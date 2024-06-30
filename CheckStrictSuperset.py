#Check Strict Superset
A = set(map(int, input().split()))
N = int(input())
count = 0
for _ in range(N):
    others = set(map(int, input().split()))
    if not (A > others):
        count += 1
        break
print(count == 0)
