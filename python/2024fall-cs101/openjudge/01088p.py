import heapq

r,c = map(int,input().split())
visited = {(x,y):0 for x in range(r) for y in range(c)}
plat = [list(map(int,input().split())) for _ in range(r)]
move = [[0,1],[1,0],[-1,0],[0,-1]]
ans = 0
q = []
heapq.heapify(q)
for i in range(r):
    for j in range(c):
        heapq.heappush(q,(plat[i][j],i,j)  )
for _ in range(r*c):
    h,x,y = heapq.heappop(q)
    for dx,dy in move:
        nx,ny = x+dx,y+dy
        if 0<=nx<r and 0<=ny<c:
            if visited[nx,ny]<visited[x,y]+1 and h<plat[nx][ny]:
                visited[nx,ny] = visited[x,y]+1
                ans = max(ans,visited[nx,ny])
print(ans+1)
