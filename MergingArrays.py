# A- Merging Arrays
n1, n2 = map(int, input().split())
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

res = nums1 + nums2
res.sort()

print(' '.join(map(str, res)))
