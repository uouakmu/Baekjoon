n=int(input())
gom = set()
cnt=0

for _ in range(n):
    word = input()
    if word != 'ENTER':
        if word not in gom:
            cnt+=1
            gom.add(word)
    elif word == 'ENTER':
        gom.clear()

print(cnt)