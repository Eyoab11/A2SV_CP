#Lists hackerrank
if __name__ == '__main__':
    N = int(input())
    res = []
    for i in range(1, N + 1): 
        opp = input().split()
        if opp[0] == 'insert':
            res.insert(int(opp[1]), int(opp[2]))
        elif opp[0] == 'print':
            print(res)
        elif opp[0] == 'remove':
            res.remove(int(opp[1]))
        elif opp[0] == 'append':
            res.append(int(opp[1]))
        elif opp[0] == 'sort':
            res.sort()
        elif opp[0] == 'pop':
            res.pop()
        elif opp[0] == 'reverse':
            res.reverse()
