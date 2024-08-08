import sys
input = sys.stdin.readline

n = int(input())
line = list(map(int,input().split()))
stack=[]
chk=1

for i in line:
    stack.append(i)
    while stack and stack[-1] == chk:
        stack.pop()
        chk += 1
    if len(stack) > 1 and stack[-1] > stack[-2]:
        print("Sad")
        sys.exit()
if stack:
	print("Sad")
else:
	print("Nice")