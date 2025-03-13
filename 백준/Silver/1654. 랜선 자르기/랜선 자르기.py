import sys
input = sys.stdin.readline

k,n = map(int,input().split())
cable = [int(input()) for _ in range(k)]

start, end = 1, max(cable)

while(start <= end):
    mid = (start+end) // 2
    cnt = 0

    for c in cable:
        cnt += c // mid
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)