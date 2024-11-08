n = input()
bignum=-1

chksum=0
for i in range(len(n)):
    chksum+=int(n[i])
if (chksum%3==0 and "0" in n):
    bignum = sorted(n,reverse=True)
    bignum = "".join(bignum)
print(bignum)