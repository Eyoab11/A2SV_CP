#2506. Count Pairs Of Similar Strings
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        number = len(words)
        
        for i in range(number):
            for j in range(i+1, number):
                if set(words[i]) == set(words[j]):
                    count += 1
        return count
