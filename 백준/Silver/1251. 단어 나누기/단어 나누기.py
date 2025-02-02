s = input().strip()
n = len(s)
result = None

for i in range(1, n-1):
    for j in range(i+1, n):
        p1 = s[:i][::-1]
        p2 = s[i:j][::-1]
        p3 = s[j:][::-1]
        
        word = p1+p2+p3
        if result is None or word < result:
            result = word
print(result)