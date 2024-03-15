# LeetCode

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = round(celsius + 273.15, 5)
        fahrenheit = round((celsius * 1.80) + 32.00, 5)
        ans = [kelvin, fahrenheit]
        return ans
