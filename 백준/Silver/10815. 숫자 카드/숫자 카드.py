import sys
import bisect

input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
cards.sort()

m = int(input())
checks = list(map(int, input().split()))

result = []
for check in checks:
    if bisect.bisect_left(cards, check) < len(cards) and cards[bisect.bisect_left(cards, check)] == check:
        result.append(1)
    else:
        result.append(0)

print(*result)