case = 1
while True:
    n = int(input())
    if n==0:
        break

    name = [input() for _ in range(n)]
    chk = [0]*n
    
    for _ in range(2*n-1):
        num,aph = input().split()
        num = int(num)

        chk[num-1] ^= 1

    for i in range(n):
        if chk[i] == 1:
            print(case,name[i])
            break
    case += 1