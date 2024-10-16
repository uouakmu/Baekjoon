n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]  # 각 집의 RGB 비용 입력

dp = [[0] * 3 for _ in range(n)]
dp[0] = costs[0]

# 각 집에 대해 최소 비용 계산
for i in range(1, n):
    dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])  # 빨강으로 칠할 경우
    dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])  # 초록으로 칠할 경우
    dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])  # 파랑으로 칠할 경우

# 마지막 집까지 칠했을 때의 최소 비용 출력
print(min(dp[n-1]))
