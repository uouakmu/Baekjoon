import sys
read = sys.stdin.readline

n, m = map(int, read().split())
a = list(map(int, read().split()))

mod = [0] * m
mod[0] = 1

sum = 0
count = 0

for i in range(n):
    sum += a[i]
    rem = sum % m
    count += mod[rem]
    mod[rem] += 1

print(count)
