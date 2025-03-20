import sys
sys.setrecursionlimit(10**6)

def dfs(y, x):
    cabbage[y][x] = 0
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < m and cabbage[ny][nx] == 1:
            dfs(ny, nx)

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    cabbage = [[0] * m for _ in range(n)]
    cnt = 0

    for _ in range(k):
        x, y = map(int, input().split())
        cabbage[y][x] = 1

    for i in range(n):
        for j in range(m):
            if cabbage[i][j] == 1:
                dfs(i, j)
                cnt += 1

    print(cnt)