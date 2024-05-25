#438. Find All Anagrams in a String
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        pctr = Counter(p)
        sctr = Counter(s[:len(p)])
        if sctr == pctr:
            result.append(0)
        for i in range(len(p), len(s)):
            sctr[s[i]] += 1
            sctr[s[i - len(p)]] -= 1
            if sctr[s[i - len(p)]] == 0:
                del sctr[s[i - len(p)]]
            if sctr == pctr:
                result.append(i - len(p) + 1)
        return result
