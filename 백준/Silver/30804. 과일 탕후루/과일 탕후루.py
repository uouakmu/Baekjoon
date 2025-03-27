import sys
input = sys.stdin.readline

n = int(input())
tang = list(map(int,input().split()))

left = 0
fruit_cnt = {}
max_len = 0

for right in range(n):
    cur_fruit = tang[right]
    
    if cur_fruit in fruit_cnt:
        fruit_cnt[cur_fruit] += 1
    else:
        fruit_cnt[cur_fruit] = 1
    
    while len(fruit_cnt) > 2:
        rem_fruit = tang[left]
        fruit_cnt[rem_fruit] -= 1

        if fruit_cnt[rem_fruit] == 0:
            del fruit_cnt[rem_fruit]

        left += 1

    max_len = max(max_len, right-left+1)

print(max_len)