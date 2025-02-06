n,m = map(int,input().split())
a = ''

for i in range(1, n+1):
    a = a + str(i)
    
print(a.count(str(m)))