dp = [0]*26
dp[0] = 1
dp[1] = 1
for i in range(2,26):
    for j in range(0,i):
        dp[i] +=dp[j]
n = int(input())
print(dp[n])