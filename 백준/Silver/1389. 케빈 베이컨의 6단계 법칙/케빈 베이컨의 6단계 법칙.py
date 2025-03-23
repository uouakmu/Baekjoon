from collections import deque

def bfs(start):
    q = deque([start])
    visited[start] = 1
    while q:
        cur = q.popleft()
        for next in node[cur]:
            if visited[next] == 0:
                visited[next] = visited[cur] + 1
                q.append(next)

n, m = map(int, input().split())
node = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

result = float('inf')
min_kevin = 0

for i in range(1, n+1):
    visited = [0] * (n+1)
    bfs(i)
    kevin = sum(visited) - 1

    if kevin < result:
        result = kevin
        min_kevin = i

print(min_kevin)