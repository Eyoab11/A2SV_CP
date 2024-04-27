#2225. Find Players With Zero or One Losses
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wins = defaultdict(int)
        losses = defaultdict(int)
        for winner, loser in matches:
            wins[winner] += 1
            losses[loser] += 1
            
        undefeated = [player for player in wins if losses[player] == 0]
        one_loss = [player for player in losses if losses[player] == 1]
        undefeated.sort()
        one_loss.sort()
        return [undefeated, one_loss]
