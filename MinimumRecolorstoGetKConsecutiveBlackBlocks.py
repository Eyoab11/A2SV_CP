#2379. Minimum Recolors to Get K Consecutive Black Blocks
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        res = float('inf')
        count = 0

        for right in range(len(blocks)):
            if blocks[right] != 'B':
                count += 1
            
            if right - left + 1 == k:
                res = min(res, count)
                if blocks[left] != 'B':
                    count -= 1
                left += 1
            
        return res
        
