# 5525

import sys
input = sys.stdin.readline

n = int(input())
slen = int(input())
s = input()

pn = 'I'+'OI'*n

cnt = 0
for i in range(slen):
  if s[i] == 'I':
    if s[i:i+(n*2+1)] == pn and i <= slen:
      cnt += 1
print(cnt)