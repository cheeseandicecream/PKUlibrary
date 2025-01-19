n = int(input())
computer =[]
time = []
for _ in range(n):
    cc,ww = map(int,input().split())
    computer.append([ww,cc])
computer.sort(reverse=True)
dp = [0]*n
dp[0] = computer[0][1]
time.append(dp[0]+computer[0][0])
for i in range(1,n):
    dp[i] = dp[i-1] + computer[i][1]
    time.append(dp[i]+computer[i][0])
print(max(time))