import sys
input = sys.stdin.readline
s = set()

for _ in range(int(input())):
    cmd = input().split()
    if cmd[0] == 'add':
        s.add(int(cmd[1]))
    elif cmd[0] == 'remove':
        s.discard(int(cmd[1]))
    elif cmd[0] == 'check':
        print(1 if int(cmd[1]) in s else 0)
    elif cmd[0] == 'toggle':
        n = int(cmd[1])
        if n in s:
            s.remove(n)
        else:
            s.add(n)
    elif cmd[0] == 'all':
        s = set(range(1, 21))
    elif cmd[0] == 'empty':
        s.clear()