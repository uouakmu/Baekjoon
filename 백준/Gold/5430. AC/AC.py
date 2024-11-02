import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    p = input().strip()
    n = int(input())
    arr = input().rstrip()[1:-1].split(",")

    if n == 0:
        arr = deque()
    else:
        arr = deque(arr)

    revercechk = False
    flag = False

    for cmd in p:
        if cmd == 'R':
            revercechk = not revercechk
        elif cmd == 'D':
            if arr:
                if revercechk:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                print('error')
                flag = True
                break

    if not flag:
        if revercechk:
            arr.reverse()
        print("[" + ",".join(arr) + "]")