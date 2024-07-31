import sys
input=sys.stdin.readline

def prime(x):
    if x<2: return False
    for i in range(2,int(x**0.5)+1):
        if x%i == 0:
            return False
    return True
    
m,n = map(int,input().split())

for i in range(m,n+1):
    if prime(i): print(i)