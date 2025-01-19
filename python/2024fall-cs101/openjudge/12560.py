def neighbor(a,b):
    if b ==1:
        if a < 2 or a > 3:
            return 0
        elif a ==2 or a==3:
            return 1
    if b ==0 and a ==3:
        return 1
    return 0

n,m = map(int,input().split())
cells = []
for i in range(n):
    cells.append(list(map(int,input().split())))
neighbors = [[0]*m for i in range(n)]
for i in range(1,n-1):
    for j in range(1,m-1):
        neighbors[i][j] = (cells[i+1][j]+cells[i-1][j]+cells[i][j-1]+
                           cells[i][j+1]+cells[i-1][j-1]+cells[i+1][j+1]+
                           cells[i-1][j+1]+cells[i+1][j-1])
neighbors[0][0]+=cells[0][1]+cells[1][0]+cells[1][1]
neighbors[0][m-1]+=cells[0][m-2]+cells[1][m-1]+cells[1][m-2]
neighbors[n-1][0]+=cells[n-2][0]+cells[n-2][1]+cells[n-1][1]
neighbors[n-1][m-1]+=cells[n-2][m-1]+cells[n-2][m-2]+cells[n-1][m-2]
for i in range(1,n-1):
    neighbors[i][0] +=cells[i-1][0]+cells[i+1][0]+cells[i-1][1]+cells[i+1][1]+cells[i][1]
    neighbors[i][m-1]+=cells[i-1][m-1]+cells[i+1][m-1]+cells[i][m-2]+cells[i-1][m-2]+cells[i+1][m-2]
for j in range(1,m-1):
    neighbors[0][j]+=cells[0][j-1]+cells[0][j+1]+cells[1][j-1]+cells[1][j+1]+cells[1][j]
    neighbors[n-1][j]+=cells[n-1][j-1]+cells[n-1][j+1]+cells[n-2][j-1]+cells[n-2][j+1]+cells[n-2][j]

for i in range(n):
    ans = []
    for j in range(m):
        ans.append(neighbor(neighbors[i][j],cells[i][j]))
    print(*ans)