#1002. Find Common Characters
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        num = len(words)
        result = []
        first = words[0]
        if num > 1:
            for i in range(1, num):
                first = self.commonString(first, words[i])
                if not first:
                    return result
        for new in first:
            result.append(new)
        return result
    
    def commonString(self, a: str, b: str) -> str:
        arr1 = [0] * 26
        arr2 = [0] * 26
        for char in a:
            arr1[ord(char) - ord('a')] += 1
        for char in b:
            arr2[ord(char) - ord('a')] += 1
        common_chars = []
        for i in range(26):
            if arr1[i] != 0 and arr2[i] != 0:
                count = min(arr1[i], arr2[i])
                common_chars.extend([chr(i + ord('a'))] * count)
        return ''.join(common_chars)
