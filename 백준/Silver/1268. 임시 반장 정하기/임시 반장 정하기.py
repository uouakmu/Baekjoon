n = int(input())
students = [list(map(int,input().split())) for _ in range(n)]
same = [[0]*n for _ in range(n)]

max_class = []

for i in range(5):
    for j in range(n):
        for k in range(j+1, n):
            if students[j][i] == students[k][i]:
                same[k][j] = 1
                same[j][k] = 1

cnt = []
for s in same:
    cnt.append(s.count(1))

print(cnt.index(max(cnt))+1)