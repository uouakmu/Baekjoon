n = int(input())

cnt = 0
while True:
    if n % 5 == 0:  
        cnt += n // 5  
        break
    n -= 2  
    cnt += 1

    if n < 0:  
        break

print(cnt if n >= 0 else -1)
