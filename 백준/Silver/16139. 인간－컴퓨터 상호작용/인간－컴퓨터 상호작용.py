import sys
input = sys.stdin.readline

s=input()
for _ in range(int(input())):
    a = input().split()
    count=0
    for i in range(int(a[1]),int(a[2])+1):
        # print("s[i]: %s, a[0]: %s"%(s[i],a[0]))
        if s[i]==a[0]:
            count +=1
            
    print(count)
    