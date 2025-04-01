from collections import deque

def bfs(n, m, grid):
    queue = deque()
    dist = [[-1] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                queue.append((i, j))
                dist[i][j] = 0
            elif grid[i][j] == 0:
                dist[i][j] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == 1 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))

    return dist

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

for row in bfs(n, m, grid):
    print(*row)