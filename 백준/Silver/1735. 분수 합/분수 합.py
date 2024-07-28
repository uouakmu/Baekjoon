def gcd(a,b):
    while b:
        a,b = b, a%b
    return a

u1, u2 = map(int,input().split())
d1, d2 = map(int,input().split())

hap = [u1*d2+u2*d1,u2*d2]
cd = gcd(hap[0],hap[1])

hap[0] //= cd
hap[1] //= cd

print(*hap)