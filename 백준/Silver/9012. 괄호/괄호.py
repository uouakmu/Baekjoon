import sys
input = sys.stdin.readline

def check(string):
    stack=[]
    for c in string:
        if c=='(':
            stack.append(c)
        else:
            if stack:
                stack.pop()
            else:
                return False
    return len(stack)==0

for i in range(int(input())):
    string=input().strip()
    if check(string):
        print("YES")
    else:
        print("NO")