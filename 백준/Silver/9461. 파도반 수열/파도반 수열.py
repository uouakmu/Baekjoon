for _ in range(int(input())):
    n = int(input())
    
    if n <= 3:
        print(1)
        continue
    
    p = [0] * (n + 1)
    p[1], p[2], p[3] = 1, 1, 1  
    
    for i in range(4, n + 1):
        p[i] = p[i - 3] + p[i - 2]
    
    print(p[n])