# 13913

# 수빈 위치: n
    # 걷거나 순간이동 가능
    # 걷기: X에서 X-1 or X+1 (1s)
    # 순간이동: X에서 2*X (1s)
# 동생 위치: k

# 수빈이와 동생이 만나는 최소시간
# 경로 출력

from collections import deque

n,k = map(int,input().split())
map = [-1]*100001
map[n] = 0
path = [-1]*100001

queue = deque()
queue.append(n)

while queue:
    current = queue.popleft()

    if current == k:
        print(map[current])

        result = []
        chk = current
        while chk != -1:
            result.append(chk)
            chk = path[chk]
        print(*result[::-1])
        break
    
    for next_c in (current-1, current+1, current*2):
        if 0 <= next_c < len(map) and map[next_c] == -1:
            map[next_c] = map[current] + 1
            path[next_c] = current
            queue.append(next_c)