for _ in range(int(input())):
    h,w,n = map(int,input().split())

    hotel = [[0]*w for _ in range(h)]
    guest = 0

    for j in range(w):
        for i in range(h):
            if hotel[i][j]==0:
                guest+=1
                hotel[i][j]=1
                if guest == n:
                    print(f"{i+1}{j+1:02d}")
                    break
        if guest == n:
            break