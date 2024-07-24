n, m = map(int, input().split())

n1 = set()
n2 = set()

for i in range(n):
    n1.add(input().strip())
for j in range(m):
    n2.add(input().strip())

result = sorted(n1 & n2)

print(len(result))
for name in result:
    print(name)