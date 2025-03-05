import sys
input = sys.stdin.readline

def multi(a,b):
    x = [[0]*k for _ in range(n)]
    for i in range(n):
        for j in range(k):
            for t in range(m):
                x[i][j] += a[i][t]*b[t][j]
    return x

n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
m,k = map(int,input().split())
b = [list(map(int,input().split())) for _ in range(m)]

for i in multi(a,b):
    print(*i)