sum = -50
l = [int(input()) for i in range(5)]
sum += min(l[0],l[1],l[2])
sum += min(l[3],l[4])
print(sum)