import sys

input = sys.stdin.readline
t = int(input().strip())
for _ in range(t):
    card = input().strip()
    total = 0

    for i, ch in enumerate(reversed(card)):
        num = int(ch)
        if i % 2 == 1:
            num *= 2
            if num >= 10:
                num -= 9
        total += num
    print("T" if total % 10 == 0 else "F")