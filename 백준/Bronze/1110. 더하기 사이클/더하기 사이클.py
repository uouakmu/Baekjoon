n = input().strip()

if len(n)==1:
    n='0'+n

org = n
cnt = 0

while(1):
    nsum = str(int(n[0])+int(n[1]))
    n = n[-1]+nsum[-1]
    cnt+=1
    if n==org:
        break
    
print(cnt)