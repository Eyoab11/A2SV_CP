#1754. Largest Merge Of Two Strings
class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        w1, w2 = 0, 0
        merged = []
        while w1 < len(word1) and w2 < len(word2):
            if word1[w1:] > word2[w2:]:
                merged.append(word1[w1])
                w1 += 1
            else:
                merged.append(word2[w2])
                w2 += 1
        while w1 < len(word1):
            merged.append(word1[w1])
            w1 += 1
        while w2 < len(word2):
            merged.append(word2[w2])
            w2 += 1
        return ''.join(merged)
