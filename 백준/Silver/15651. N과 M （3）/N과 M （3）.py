n, m = map(int, input().split())
s = []

def bt():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, n + 1):
        s.append(i)
        bt()
        s.pop()

bt()