import heapq

m,n,p = map(int,input().split())
plat = [['#' for _ in range(n+2)] for _ in range(m+2)]
for i in range(1,m+1):
    plat[i][1:n+1] = input().split()
move = [[0,1],[0,-1],[1,0],[-1,0]]
ans = float('inf')

def climb(x1,y1,x2,y2,plat,dp):
    if plat[x_1][y_1] == '#'or plat[x_2][y_2] == '#':
        return 'NO'
    heap = [(0,x1,y1)]
    found = False

    while heap:
        cost,x,y = heapq.heappop(heap)
        if x == x2 and y == y2:
            found = True
            return cost
        for dx,dy in move:
            nx,ny = x + dx,y + dy
            if plat[nx][ny] != '#':
                n_cost = cost + abs(int(plat[nx][ny])-int(plat[x][y]))
                if n_cost < dp[nx][ny]:
                    heapq.heappush(heap,(n_cost,nx,ny))
                    dp[nx][ny] = n_cost
    if not found:
        return 'NO'

for _ in range(p):
    ans = float('inf')
    dp = [[float('inf') for _ in range(n+2)] for _ in range(m+2)]
    x_1,y_1,x_2,y_2 = map(int,input().split())
    x_1 +=1; y_1+=1; x_2+=1; y_2+=1
    print(climb(x_1,y_1,x_2,y_2,plat,dp))