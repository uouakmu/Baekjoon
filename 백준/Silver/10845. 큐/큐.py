from collections import deque
import sys
input = sys.stdin.readline

queue = deque()

for _ in range(int(input())):
    cmd = input().rstrip()
    if cmd.startswith("push"):
        queue.append(int(cmd[5:]))
    else:
        if cmd == "pop":
            if queue:
                print(queue[0])
                queue.popleft()
            else:
                print(-1)
        if cmd == "size":
            print(len(queue))
        if cmd == "empty":
            if queue: print(0)
            else: print(1)
        if cmd == "front":
            if queue:
                print(queue[0])
            else: print(-1)
        if cmd == "back":
            if queue:
                print(queue[-1])
            else: print(-1)