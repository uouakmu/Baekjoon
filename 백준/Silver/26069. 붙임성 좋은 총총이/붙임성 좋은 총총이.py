import sys
input = sys.stdin.readline

dance = {'ChongChong'}

for i in range(int(input())):
    a,b=map(str,input().split())
    if a in dance:
        dance.add(b)
    if b in dance:
        dance.add(a)

print(len(dance))