def dfs(y, x):
    house[y][x] = 0
    global cnt
    cnt += 1
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < n and house[ny][nx] == 1:
            dfs(ny, nx)

n = int(input())
house = [list(map(int, input().strip())) for _ in range(n)]
res = []

for i in range(n):
    for j in range(n):
        if house[i][j] == 1:
            cnt = 0
            dfs(i, j)
            res.append(cnt)

res.sort()
print(len(res), *res, sep="\n")
