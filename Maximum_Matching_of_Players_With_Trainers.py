# 2410. Maximum Matching of Players With Trainers
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        n_players = len(players)
        left = 0
        right = 0
        count = 0
        while left < n_players and right < len(trainers):
            if players[left] <= trainers[right]:
                count += 1
                left += 1
                right += 1
            else:
                right += 1
        return count
