import math

n= int(input())
s = [int(input()) for _ in range(n)]

dist = [s[i+1] - s[i] for i in range(n-1)]

gcd=dist[0]
for d in dist[1:]:
    gcd = math.gcd(gcd,d)

ans = 0
for d in dist:
    ans += (d//gcd) - 1

print(ans)