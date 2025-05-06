import sys
from collections import deque

input = sys.stdin.readline

m,n = map(int,input().split())
tomatoes = [list(map(int,input().split())) for _ in range(n)]

def bfs(graph, x, y):
    queue = deque()

    for i in range(n):  # 익은 토마토 큐에 저장
        for j in range(m):
            if tomatoes[i][j] == 1:
                queue.append((i,j))
    
    # 탐색 방향
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if tomatoes[nx][ny] == 0:
                    tomatoes[nx][ny] = tomatoes[x][y] + 1
                    queue.append((nx,ny))

    cnt = 0
    for row in tomatoes:
        for val in row:
            if val == 0:    # 안 익은 토마토가 하나라도 있다면
                return -1
        cnt = max(cnt, max(row))    # 마지막으로 끝난 일수

    return cnt-1

print(bfs(m,n,tomatoes))