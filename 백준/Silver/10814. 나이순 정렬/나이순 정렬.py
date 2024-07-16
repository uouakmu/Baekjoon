n = int(input())
users = []
for _ in range(n):
    age,name = input().split()
    users.append([int(age),name])

for i in sorted(users,key=lambda x : x[0]):
    print(i[0],i[1])