s=[]
ans=[]
for i in range(int(input())):
    s.append(input())
ans = list(s[0])
for i in range(1,len(s)):
    for j in range(len(ans)):
        if s[i][j] != ans[j]:
            ans[j] = '?'
print("".join(ans))