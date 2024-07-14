n=int(input())
coordinates = []
for _ in range(n):
    x,y=map(int,input().split())
    coordinates.append((x, y))
coordinates.sort(key = lambda coord: (coord[1], coord[0]))
for t in range(n):
    print(*coordinates[t])