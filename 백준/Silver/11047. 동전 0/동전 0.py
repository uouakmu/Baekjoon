import sys
input = sys.stdin.readline

n,k = map(int,input().split())

cnt = 0
coins = [int(input()) for _ in range(n)]

for c in coins[::-1]:
    if k>=c:
        cnt += k//c
        k %=c

print(cnt)