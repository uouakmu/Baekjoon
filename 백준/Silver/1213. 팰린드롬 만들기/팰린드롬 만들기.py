from collections import Counter

s = sorted(input().strip())
cnt = Counter(s)
odd = ''.join(char for char in cnt if cnt[char] % 2)
if len(odd) > 1:
    print("I'm Sorry Hansoo")
else:
    half = ''.join(char * (cnt[char] // 2) for char in cnt)
    print(half + (odd if odd else '') + half[::-1])
