nums = []
cards = list(i for i in range(1,int(input())+1))

while(len(cards) != 1):
    nums.append(cards.pop(0))
    cards.append(cards.pop(0))

print(*nums,*cards)