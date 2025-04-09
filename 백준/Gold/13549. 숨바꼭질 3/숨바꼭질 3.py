from collections import deque

n, k = map(int, input().split())
map = [-1] * 100001  # 방문 안 한 곳은 -1
map[n] = 0  # 시작점 시간은 0

queue = deque()
queue.append(n)

while queue:
    current = queue.popleft()

    if current == k:
        print(map[current])
        break

    for next_c in (current * 2, current - 1, current + 1):
        if 0 <= next_c < len(map) and map[next_c] == -1:
            if next_c == current * 2:
                map[next_c] = map[current]
                queue.appendleft(next_c)  # 0초인 이동은 앞으로!
            else:
                map[next_c] = map[current] + 1
                queue.append(next_c)  # 1초 걸리는 이동
