n = int(input())

dp = [0]*n
dp[0] = 1

if n>=2:
    dp[1] = 3
    for i in range(2,n):
        dp[i] = dp[i-1] + 2*dp[i-2]

print(dp[n-1] % 10007)