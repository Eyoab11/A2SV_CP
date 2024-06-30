#973. K Closest Points to Origin
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(points)):
            x, y = points[i]
            distance = math.sqrt(x**2 + y**2)
            points[i].append(distance)
        points.sort(key = lambda x:x[2])
        res = []
        for i in range(k):
            res.append([points[i][0], points[i][1]])
        return res
