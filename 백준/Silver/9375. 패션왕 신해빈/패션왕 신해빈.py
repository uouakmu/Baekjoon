for _ in range(int(input())):
    n = int(input())
    wears = {}

    for _ in range(n):
        wear = list(input().split())
        if wear[1] in wears:
            wears[wear[1]].append(wear[0])
        else:
            wears[wear[1]] = [wear[0]]

    cnt = 1

    for w in wears:
        cnt *= (len(wears[w]) + 1)

    print(cnt-1)