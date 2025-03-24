import sys
input = sys.stdin.readline

N = int(input())
color = [list(map(int,input().split())) for _ in range(N)]
w_cnt, b_cnt = 0,0

def div(x,y,n):
    global w_cnt,b_cnt
    cnt = 0
    for i in range(x,x+n):
        for j in range(y, y+n):
            if color[i][j]:
                cnt += 1
    if not cnt:
        w_cnt += 1
    elif cnt == n**2:
        b_cnt += 1
    else:
        div(x, y, n//2)
        div(x+n//2, y, n//2)
        div(x, y+n//2, n//2)
        div(x+n//2, y+n//2, n//2)
    return

div(0,0,N)
print(w_cnt)
print(b_cnt)