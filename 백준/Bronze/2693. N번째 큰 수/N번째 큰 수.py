for _ in range(int(input())):
    a = list(map(int,input().split()))
    for i in range(2):
        a.remove(max(a))
    print(max(a))
