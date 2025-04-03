from math import lcm

def solve(m,n,x,y):
    k = x
    while k <= lcm(m,n):
        if (k-x)%m == 0 and (k-y)%n == 0:
            return k
        k += m
    return -1

for _ in range(int(input())):
    M,N,x,y = map(int,input().split())
    print(solve(M,N,x,y))