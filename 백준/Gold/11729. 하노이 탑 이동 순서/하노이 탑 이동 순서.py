def hanoi(n, start, end, aux):
    if n == 1:
        print(f"{start} {end}")
        return
    hanoi(n-1, start, aux, end)
    print(f"{start} {end}")
    hanoi(n-1, aux, end, start)

n = int(input())
print(2**n - 1)
hanoi(n, 1, 3, 2)