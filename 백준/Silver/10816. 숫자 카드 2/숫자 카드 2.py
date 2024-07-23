import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
l1 = list(map(int, input().split()))
m = int(input())
l2 = list(map(int, input().split()))

counter = Counter(l1)
result = [counter[num] for num in l2]

print(*result)