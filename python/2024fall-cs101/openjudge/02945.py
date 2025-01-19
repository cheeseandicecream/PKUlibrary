k = int(input())
missiles = list(map(int, input().split()))

def compete(i,n,l):
    m = 0
    for j in range(i+1,n):
        if l[i]>=l[j]:
            m = max(m,compete(j,n,l)+1)
    if m ==0:
        return 1
    return m

ans = 0
for i in range(k):
    ans = max(ans, compete(i,k,missiles))
print(ans)