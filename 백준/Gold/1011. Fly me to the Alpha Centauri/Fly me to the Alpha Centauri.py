for _ in range(int(input())):
    x,y = map(int,input().split())
    d = y-x
    cnt = 0
    move = 1
    total_move = 0

    while(total_move < d):
        cnt+=1
        total_move += move
        if(cnt%2 == 0):
            move += 1

    print(cnt)