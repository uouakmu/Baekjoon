n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
s = 0
for i in range(n):
    s += a[i]*max(b)
    b.remove(max(b))

print(s)