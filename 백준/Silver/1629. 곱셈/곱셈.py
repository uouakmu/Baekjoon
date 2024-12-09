def mul(a,b,c):
    if b==1:
        return a%c
    else:
        ans = mul(a, b//2, c)
        if b%2==0:
            return (ans*ans)%c
        else:
            return (ans*ans*a)%c

a,b,c= map(int,input().split())
print(mul(a,b,c))