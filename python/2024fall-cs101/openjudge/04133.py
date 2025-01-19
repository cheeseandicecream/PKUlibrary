dp = [[0]*1025 for i in range(1025)]

d = int(input())
n = int(input())
ans = 0
m=0
for _ in range(n):
    x,y,i = map(int,input().split())
    for a in range(-d,d+1):
        for b in range(-d,d+1):
            if x+a>=1025 or x+a<0 or y+b>=1025 or y+b<0:
                continue
            dp[x+a][y+b] +=i
for i in range(1025):
    for j in range(1025):
        if ans<dp[i][j]:
            m=1
        elif ans==dp[i][j]:
            m+=1
        ans = max(ans,dp[i][j])

print(f'{m} {ans}')