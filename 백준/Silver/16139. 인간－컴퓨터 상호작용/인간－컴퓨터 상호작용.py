import sys
input = sys.stdin.readline

s = input().rstrip()
aph = [[0] * 26 for _ in range(len(s) + 1)]

for i in range(len(s)):  
    for j in range(26):
        aph[i + 1][j] = aph[i][j]  
    aph[i + 1][ord(s[i]) - 97] += 1  

for _ in range(int(input())):
    arr = input().split()
    res = aph[int(arr[2]) + 1][ord(arr[0]) - 97] - aph[int(arr[1])][ord(arr[0]) - 97]
    print(res)