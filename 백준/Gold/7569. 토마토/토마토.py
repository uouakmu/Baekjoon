# 7569 토마토2

import sys
from collections import deque

input = sys.stdin.readline

m,n,h = map(int,input().split())
tomatoes = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]

def bfs():
    queue = deque()

    for z in range(h):
        for x in range(n):
            for y in range(m):
                if tomatoes[z][x][y] == 1:
                    queue.append((x,y,z))

    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    while queue:
        x,y,z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if tomatoes[nz][nx][ny] == 0:
                    tomatoes[nz][nx][ny] = tomatoes[z][x][y] + 1
                    queue.append((nx,ny,nz))

    cnt = 0
    for z in range(h):
        for x in range(n):
            for y in range(m):
                if tomatoes[z][x][y] == 0:
                    return -1
                cnt = max(cnt, tomatoes[z][x][y])
    return cnt-1
print(bfs())