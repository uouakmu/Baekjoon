n, m = map(int, input().split())
s = []

def bt(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(start, n + 1):
        s.append(i)
        bt(i)
        s.pop()

bt(1)