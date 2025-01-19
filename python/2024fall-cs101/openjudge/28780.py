n,m = map(int,input().split())
coins = list(map(int,input().split()))
dp = [0]+[float('inf') for i in range(m)]
for coin in coins:
    for i in range(coin,m+1):
        dp[i]= min(dp[i],dp[i-coin]+1)
print(dp[m])