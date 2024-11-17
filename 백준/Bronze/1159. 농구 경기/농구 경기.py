n = int(input())
array = [0] * 26

for i in range(n):
    s = input()
    if s and s[0].islower():
        array[ord(s[0]) - 97] += 1

result = ""
for i in range(26):
    if array[i] >= 5:
        result += chr(i + 97)

print(result if result else "PREDAJA")