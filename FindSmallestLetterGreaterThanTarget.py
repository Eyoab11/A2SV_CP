#744. Find Smallest Letter Greater Than Target
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        lower = 0
        upper = len(letters) - 1
        while lower <= upper:
            mid = (upper + lower) // 2
            if letters[mid] > target:
                upper = mid - 1
            else:
                lower = mid + 1
        return letters[lower % len(letters)]
