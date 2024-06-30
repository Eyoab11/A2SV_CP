#1833. Maximum Ice Cream Bars
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        
        if costs[0] > coins:
            return 0
        
        for cost in costs:
            if coins >= cost:
                coins -= cost
                count += 1
            else:
                break
        
        return count
