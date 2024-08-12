import math

for _ in range(int(input())):
    n, m = map(int, input().split())
    result = math.comb(m, n)
    print(result)