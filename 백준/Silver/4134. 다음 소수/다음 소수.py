import sys
input=sys.stdin.readline

def prime(x):
    for i in range(2,int(x**0.5)+1):
        if x%i == 0:
            return False
    return True
    
for i in range(int(input())):
    n=int(input())
    while True:
        if n==0 or n==1:
            print(2)
            break
        if prime(n):
            print(n)
            break
        else: n+=1