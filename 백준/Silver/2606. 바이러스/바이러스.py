n = int(input())
v = int(input())
graph = [[] for i in range(n+1)]
visited = [0]*(n+1)

for i in range(v):
    a,b = map(int,input().split())
    graph[a] += [b]
    graph[b] += [a]

def dfs(v):
    visited[v] = 1
    for dx in graph[v]:
        if visited[dx] == 0:
            dfs(dx)
dfs(1)
print(sum(visited)-1)