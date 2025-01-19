n = int(input())
presents = list(map(int, input().split()))

def find(l,n):
    for i in range(1,n):
        for j in range(i+1):
            if (l[n+j-i]-l[j])%520 ==0:
                return n-i
    return 0

if sum(presents)%520==0:
    print(n*520)
else:
    dp = [0]*(n+1)
    for i in range(1,n+1):
        dp[i] = dp[i-1]+presents[i-1]
    print(int(find(dp,n)*520))