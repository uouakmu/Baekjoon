def self_n(n):
    return n + sum(map(int, str(n)))

results = set(self_n(i) for i in range(1, 10001))
all_n = set(range(1, 10001))

self_n = sorted(all_n - results)

for num in self_n:
    print(num)