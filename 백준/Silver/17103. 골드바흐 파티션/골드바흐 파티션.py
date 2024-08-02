import sys
input = sys.stdin.readline

prime = [False, False] + [True]*999999

for i in range(2, 1000001):
    if prime[i]:
        for j in range(i*2, 1000001,i):
            prime[j]=False

for _ in range(int(input())):
    count =0
    n=int(input())
    for i in range(2, n//2+1):
        if prime[i] and prime[n-i]: count +=1
    print(count)