n,m = map(int,input().split())
sites = {}

for _ in range(n):
    site, pw = input().split()
    sites[site] = pw

for _ in range(m):
    link = input()
    print(sites[link])