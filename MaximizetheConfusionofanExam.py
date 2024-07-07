#2024. Maximize the Confusion of an Exam
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def helper(letter):
            left = 0
            count = 0
            res = 0
            for i in range(len(answerKey)):
                if answerKey[i] != letter:
                    count += 1
                while count > k:
                    if answerKey[left] != letter:
                        count -= 1
                    left += 1
                res = max(res, i - left + 1)
            return res
        return max(helper('T'), helper('F'))
