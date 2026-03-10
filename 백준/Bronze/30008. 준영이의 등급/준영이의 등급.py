def grade(score):
    if 0 <= score <= 4:
        return 1
    elif 4 < score <= 11:
        return 2
    elif 11 < score <= 23:
        return 3
    elif 23 < score <= 40:
        return 4
    elif 40 < score <= 60:
        return 5
    elif 60 < score <= 77:
        return 6
    elif 77 < score <= 89:
        return 7
    elif 89 < score <= 96:
        return 8
    return 9


n, k = map(int, input().split())
scores = list(map(int, input().split()))
res = []

for s in scores:
    avr = s * 100 // n
    res.append(grade(avr))

print(*res)