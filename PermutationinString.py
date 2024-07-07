#567. Permutation in String
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mps1 = Counter(s1)
        mps2 = Counter(s2[:len(s1)])
        l = 0
        for i in range(len(s1),len(s2)):
            if mps1 == mps2:
                return True
            mps2[s2[l]] -= 1
            if mps2[s2[l]] == 0:
                del mps2[s2[l]]
            mps2[s2[i]] += 1
            l += 1
        if mps1 == mps2:
            return True
        return False
