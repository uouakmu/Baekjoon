for _ in range(int(input())):
    a,b = map(int, input().split())
    a %= 10
    if a == 0:
        print(10)
    else:
        arr = []
        chk = a
        while chk not in arr:
            arr.append(chk)
            chk = (chk * a) % 10
        print(arr[(b - 1) % len(arr)])