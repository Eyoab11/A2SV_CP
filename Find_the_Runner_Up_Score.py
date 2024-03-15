# HackerRank

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    

unique_scores = set(arr)
sorted = sorted(unique_scores, reverse=True)

runner_up_score = sorted[1]

print(runner_up_score)
