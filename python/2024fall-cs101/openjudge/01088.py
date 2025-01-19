from collections import deque

r,c = map(int,input().split())
visited = {(x,y):0 for x in range(r) for y in range(c)}
plat = [list(map(int,input().split())) for _ in range(r)]
move = [[0,1],[1,0],[-1,0],[0,-1]]
ans = 0

def bfs(r,c,x,y,k):
    global visited
    global ans
    q = deque()
    q.append((x,y))
    while q:
        for _ in range(len(q)):
            x,y = q.popleft()
            for dx,dy in move:
                nx,ny = x+dx,y+dy
                if 0<=nx<r and 0<=ny<c:
                    if plat[nx][ny]>plat[x][y] and k+1>visited[(nx,ny)]:
                        visited[(nx,ny)] = k+1
                        q.append((nx,ny))
        k +=1
    ans = max(ans,k)
    return

for i in range(r):
    for j in range(c):
        if visited[(i,j)] == 0:
            bfs(r,c,i,j,visited[(i,j)])
print(ans)