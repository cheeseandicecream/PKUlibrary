n,m = map(int,input().split())
d=[[0]*(m+2)]
for i in range(n):
    d.append([0]+list(map(int,input().split()))+[0])
d.append([0]*(m+2))
ans = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if d[i][j]==1:
            ans +=4 - d[i+1][j]-d[i-1][j]-d[i][j+1]-d[i][j-1]
print(ans)

