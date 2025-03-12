for _ in range(int(input())):
    n,m = map(int,input().split())
    priority = list(map(int,input().split()))

    result = 1
    while priority:
        if priority[0] < max(priority):
            priority.append(priority.pop(0))
        else:
            if m==0: break
            priority.pop(0)
            result += 1
        
        m = m-1 if m>0 else len(priority)-1
    print(result)