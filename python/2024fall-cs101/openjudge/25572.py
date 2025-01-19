from collections import deque

n = int(input())
plat = [[1 for _ in range(n+2)] for _ in range(n+2)]
for i in range(1,n+1):
    plat[i][1:n+1] = map(int, input().split())
move = [[0,1],[0,-1],[1,0],[-1,0]]

def dfs(plat,n):
    out = []
    for i in range(1,n+1):
        for j in range(1,n+1):
            if plat[i][j] == 5:
                out.append((i,j))
    return out

def bfs(l):
    q = deque()
    x1,y1 = l[0]
    x2,y2 = l[1]
    q.append((x1,y1,x2,y2))
    while q:
        x1, y1, x2, y2 = q.popleft()
        if plat[x1][y1] == 9 or plat[x2][y2] == 9:
            return True
        for dx,dy in move:
            nx1,ny1,nx2,ny2 = x1 + dx,y1 + dy,x2 + dx,y2 + dy
            if plat[nx1][ny1] !=1 and plat[nx2][ny2]!=1:
                q.append((nx1,ny1,nx2,ny2))
        plat[x1][y1],plat[x2][y2] = 1,1
    return False

if bfs(dfs(plat,n)):
    print('yes')
else:
    print('no')


