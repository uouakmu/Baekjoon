a, b = map(str, input().split())
max_len = 0
if len(a) > len(b) :
  max_len = len(a)
  b = '0' * (len(a) - len(b)) + b
elif len(a) < len(b) :
  max_len = len(b)
  a = '0' * (len(b) - len(a)) + a
else :
  max_len = len(b)

result = ''
for i in range(max_len) :
  result += str(int(a[i]) + int(b[i]))

print(result)