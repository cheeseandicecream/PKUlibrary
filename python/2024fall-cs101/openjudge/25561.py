n,m = map(int,input().split())
stores = [input().split() for _ in range(n)]
cheaps = [input().split() for _ in range(m)]
buy = [0]*m
ans = float('inf')
def dfs(i,k,l):
    global ans
    if i == n:
        jian = 0
        for j in range(m):
            dan = 0
            for cheap in cheaps[j]:
                x,y = map(int,cheap.split('-'))
                if l[j] >=x:
                    dan = max(dan,y)
            jian += dan
        ans = min(ans,k-(k//300)*50-jian)
        return
    else:
        for store in stores[i]:
            a,b = map(int,store.split(':'))
            l[a-1] +=b
            dfs(i+1,k+b,l[:])
            l[a-1] -=b
dfs(0,0,buy[:])
print(ans)