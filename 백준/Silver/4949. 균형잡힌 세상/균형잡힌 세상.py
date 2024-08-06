import sys
input = sys.stdin.readline

def check(string):
    stack=[]
    for c in string:
        if c=='(' or c=='[':
            stack.append(c)
        elif c == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
        elif c == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return False
    return len(stack) == 0

while True:
    string=input().rstrip()
    if string == '.': break
    if check(string):
        print("yes")
    else:
        print("no")