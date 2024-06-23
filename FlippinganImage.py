#832. Flipping an Image
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            left = 0
            right = len(image[i]) - 1
            while left < right:
                image[i][left], image[i][right] = image[i][right], image[i][left]
                left += 1
                right -= 1
                
        for i in range(len(image)):
            for j in range(len(image[i])):
                if image[i][j] == 0:
                    image[i][j] = 1
                elif image[i][j] == 1:
                    image[i][j] = 0

        return image
