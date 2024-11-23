count = 0
doc = input()
find = input()

i = 0
while (i <= len(doc)-len(find)):
    if doc[i:i+len(find)] == find:
        count += 1
        i += len(find)
    else:
        i += 1

print(count)