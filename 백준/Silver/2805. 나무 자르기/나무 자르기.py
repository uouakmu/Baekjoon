import sys
input = sys.stdin.readline

n,m = map(int,input().split())
heights = list(map(int,input().split()))
start, end = 1, max(heights)

while (start <= end):
    mid = (start+end) // 2
    cnt = sum(t - mid for t in heights if t > mid)
    
    if cnt >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)