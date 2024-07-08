#904. Fruit Into Baskets
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        baskets = {}
        res = 0
        left = 0
        
        for i in range(len(fruits)):
            if fruits[i] in baskets:
                baskets[fruits[i]] += 1
            else:
                baskets[fruits[i]] = 1

            while len(baskets) > 2:
                baskets[fruits[left]] -= 1
                if baskets[fruits[left]] == 0:
                    del baskets[fruits[left]]
                left += 1
            res = max(res, i - left + 1)
        return res
