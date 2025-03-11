r = 31
m = 1234567891

l = int(input())
aph = input()
nums = list((ord(i)-96) for i in aph)

h=0
for i in range(l):
    h += nums[i] * r**(i)
h %= m
print(h)