#2418. Sort the People
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        max_height = max(heights)
        count = [0] * (max_height + 1)
        for height in heights:
            count[height] += 1
        sorted_names = []
        for i in range(max_height, 0, -1):
            while count[i] > 0:
                sorted_names.append(names[heights.index(i)])
                count[i] -= 1
        return sorted_names
