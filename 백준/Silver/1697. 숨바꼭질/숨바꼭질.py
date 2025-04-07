# 1697

# 수빈 위치: n
    # 걷거나 순간이동 가능
    # 걷기: X에서 X-1 or X+1 (1s)
    # 순간이동: X에서 2*X (1s)
# 동생 위치: k

# 수빈이와 동생이 만나는 최소시간
# 수빈이 기준, 각 위치까지 최소시간을 구해두면 될듯

from collections import deque

n,k = map(int,input().split())
graph = [0] * (max(n,k)*2+1)

queue = deque()
queue.append(n)

while queue:
    current = queue.popleft()

    if current == k:
        print(graph[current])
        break
    
    for next_c in (current-1, current+1, current*2):
        if 0<= next_c < len(graph) and graph[next_c] == 0:
            graph[next_c] = graph[current] + 1
            queue.append(next_c)