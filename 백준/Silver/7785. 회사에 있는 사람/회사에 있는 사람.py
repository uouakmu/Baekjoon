n = int(input())
log = {}

for _ in range(n):
    name, work = input().split()
    if work == "enter":
        log[name] = True
    else:
        if name in log:
            del log[name]

for name in sorted(log.keys(), reverse=True):
    print(name)
