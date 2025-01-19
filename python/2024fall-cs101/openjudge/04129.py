from collections import deque

def find(l,r,c,a):
    for i in range(r):
        for j in range(c):
            if l[i][j] ==a:
                return i,j

def walk(r,c,x1,y1,k,plat):
    move = [[0,1],[1,0],[-1,0],[0,-1]]
    found = False
    q = deque([(x1,y1)])
    time =0
    visited = [[[False for _ in range(c)] for _ in range(r)] for _ in range(k)]
    while q:
        time += 1
        for _ in range(len(q)):
            x,y = q.popleft()
            if plat[x][y] =='E':
                return time-1
            for dx,dy in move:
                nx,ny = x+dx,y+dy
                if 0<=nx<r and 0<=ny<c:
                    if time%k ==0 or plat[nx][ny]!='#':
                        if not visited[time%k][nx][ny]:
                            q.append((nx,ny))
                            visited[time%k][nx][ny]=True
    if not found:
        return 'Oop!'

t = int(input())
for _ in range(t):
    r,c,k = map(int,input().split())
    plat = []
    for _ in range(r):
        plat.append(input())
    x1,y1 = find(plat,r,c,'S')
    print(walk(r,c,x1,y1,k,plat))