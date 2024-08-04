import sys

N = int(sys.stdin.readline())
ST = []
for i in range(N):
    op = sys.stdin.readline().split()
    if op[0] == '1':
        ST.append(int(op[-1]))
    elif op[0] == '2':
        if ST:
            print(ST.pop(-1))
            continue
        print(-1)
    elif op[0] == '3':
        print(len(ST))
    elif op[0] == '4':
        if ST:
            print(0)
            continue
        print(1)
    elif op[0] == '5':
        if ST:
            print(ST[-1])
            continue
        print(-1)