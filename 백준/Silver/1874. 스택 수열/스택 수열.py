import sys
input = sys.stdin.readline

stack, ans, chk = [], [], True
now = 1

for _ in range(int(input())):
    num = int(input())
    while now <= num:
        stack.append(now)
        ans.append('+')
        now += 1
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        chk = False

if chk:
    for i in ans:
        print(i)
else: print('NO')