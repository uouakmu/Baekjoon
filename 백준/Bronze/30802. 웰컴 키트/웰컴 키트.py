n = int(input())
size = list(map(int,input().split()))
t,p = map(int,input().split())

tsum = 0
for i in size:
    if i==0:
        continue
    elif i<=t:
        tsum+=1
    elif i%t == 0:
        tsum += i//t
    else:
        tsum += i//t+1

psum = n//p
pen = n%p

print(tsum)
print(f'{psum} {pen}')