import sys
sys.setrecursionlimit(10**6)

def dfs(x,y):
    global cnt
    visited[x][y] = True

    if campus[x][y] == 'P':
        cnt += 1
    
    dy,dx = [0,0,-1,1], [1,-1,0,0]

    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]

        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] != True and campus[nx][ny] != 'X':
            dfs(nx,ny)

n,m = map(int,input().split())
campus = [list(input()) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

x,y = -1,-1
for i in range(n):
    for j in range(m):
        if campus[i][j]=='I':
            x,y = i,j
            break
    if x != -1:
        break

cnt = 0
dfs(x,y)

print(cnt if cnt>0 else 'TT')