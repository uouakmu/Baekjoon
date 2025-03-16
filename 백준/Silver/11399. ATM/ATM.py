n = int(input())
time = sorted(list(map(int,input().split())))

if n==1: print(time[0])
else:
    for i in range(1, n):
        time[i] = time[i-1]+time[i]
    print(sum(time))