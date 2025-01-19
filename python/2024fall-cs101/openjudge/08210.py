ans = 0
l,n,m = map(int,input().split())
rocks = [0]*(n+2)
rocks[n+1] = l
for i in range(1,n+1):
    rocks[i] = int(input())

def jump(dp,m,n,l):
    now = 0
    k =0
    for i in range(1,n+2):
        if dp[i]-now <l:
            k+=1
        else:
            now = dp[i]
    if k>m:
        return True
    else:
        return False

min1 = 0
max1 = l+1
while max1>min1:
    mid = (min1+max1)//2
    if jump(rocks,m,n,mid):
        max1 = mid
    else:
        ans = mid
        min1 = mid+1
print(ans)