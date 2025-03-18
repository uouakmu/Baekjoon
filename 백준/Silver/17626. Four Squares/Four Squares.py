def solve():
    n = int(input())
    sqr = n**0.5

    if sqr.is_integer():
        return 1
        
    for i in range(int(sqr), 0, -1):
        if ((n - i**2)**0.5).is_integer():
            return 2

    for i in range(int(sqr),0,-1):
        for j in range(int((n-i**2)**0.5),0,-1):
            if ((n - i**2 - j**2)**0.5).is_integer():
                return 3
    
    return 4

print(solve())