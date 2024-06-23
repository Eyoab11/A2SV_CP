#1859. Sorting the Sentence
class Solution:
    def sortSentence(self, s: str) -> str:
        sentence = s.split()
        s = sorted(sentence, key = lambda word: int(word[-1]))
        words = [word[:-1] for word in s]
        return ' '.join(words)
