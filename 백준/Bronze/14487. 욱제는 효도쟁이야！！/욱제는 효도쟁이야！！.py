N = int(input())
cost = list(map(int,input().split()))
S = sum(cost)
lst = []
for i in range(N):
    lst.append(S-cost[i])
print(min(lst))