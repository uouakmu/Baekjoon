num = [0] * 10
n = input()
for i in n:
    num[int(i)] +=1
num[6] = (num[6]+num[9]+1)//2
num[9] = 0
print(max(num))