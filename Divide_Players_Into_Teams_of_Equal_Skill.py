#2491. Divide Players Into Teams of Equal Skill

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        left = 0
        right = n-1
        count = 0
        target = skill[left] + skill[right]
        while right > left:
            if skill[left] + skill[right] == target:
                count+= skill[left] * skill[right]
                left += 1
                right -= 1
            else:
                count = -1
                break
        return count
                    
            
