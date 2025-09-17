import sys
input = sys.stdin.readline

# 입력
N = int(input())
page = list(map(int, input().split()))
study = list(map(int, input().split()))

res = 0
for i, j in zip(page, study):
    if i-j <= 0:
        res += 1

print(res)