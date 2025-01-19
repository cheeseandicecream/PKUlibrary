N,B = map(int,input().split())
prices = list(map(int,input().split()))
weights = list(map(int,input().split()))

dp = [0]*(B+1)
for i in range(N):
    for j in range(B,weights[i]-1,-1):
        dp[j]= max(dp[j],dp[j-weights[i]]+prices[i])
print(dp[-1])