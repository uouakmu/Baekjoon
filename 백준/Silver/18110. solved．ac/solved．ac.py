import sys
input = sys.stdin.readline

def roundUp(num):
    if(num-int(num)) >= 0.5:
        return int(num)+1
    else:
        return int(num)

n = int(input().rstrip())
if n==0:
    print(0)
else:
    level=[]
    level = [int(input()) for _ in range(n)]
    level.sort()

    exc = roundUp(n*0.15)

    result = roundUp(sum(level[exc:n-exc])/len(level[exc:n-exc]))
    print(result)