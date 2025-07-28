# 1158번 요세푸스 문제
from collections import deque

ans = []
n,k = map(int, input().split())
queue = deque(range(1, n+1))

while queue:
    queue.rotate(-(k-1))
    ans.append(queue.popleft())
print(f"<{", ".join(map(str,ans))}>")