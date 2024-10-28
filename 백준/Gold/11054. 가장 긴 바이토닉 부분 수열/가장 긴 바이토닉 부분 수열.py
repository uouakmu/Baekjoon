import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

ldp = [1] * n
rdp = [1] * n

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            ldp[i] = max(ldp[i], ldp[j]+1)

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if arr[j] < arr[i]:
            rdp[i] = max(rdp[i], rdp[j]+1)

maxl = 0
for i in range(n):
    maxl = max(maxl, ldp[i] + rdp[i] - 1)

print(maxl)