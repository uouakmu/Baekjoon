from collections import deque

def dfs(v):
    visited[v] = True
    print(v, end=" ")
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in sorted(graph[v]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, start = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
dfs(start)
print()

visited = [False] * (n + 1)
bfs(start)
