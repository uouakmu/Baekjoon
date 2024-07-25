n, m = map(int, input().split())

n1 = set(map(int, input().split()))
n2 = set(map(int, input().split()))

ans =  n1.symmetric_difference(n2)
print(len(ans))