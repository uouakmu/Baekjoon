book={}
for _ in range(int(input())):
    name = input()
    if name not in book:
        book[name] = 1
    else:
        book[name] += 1

Lsell = max(book.values())

best = []
for key, value in book.items():
    if value == Lsell:
        best.append(key)

best = sorted(best)
print(best[0])