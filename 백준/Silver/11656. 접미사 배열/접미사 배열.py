s = input()
array=[]

for i in range(len(s)):
    array.append(s[i:])
array.sort()
for i in range(len(array)):
    print(array[i])