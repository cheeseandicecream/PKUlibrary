dp = [0]*5001
dp[1] = 1
dp[2] = 2
for i in range(3,5001):
    dp[i] = dp[i-1] + dp[i-2]
m = int(input())
print(dp[m])