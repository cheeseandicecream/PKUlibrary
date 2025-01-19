import sys
from collections import deque
data = sys.stdin.read().split()

move = [[1,0],[0,1],[-1,0],[0,-1]]

k = int(data[0])
id = 1
for _ in range(k):
    m,n = int(data[id]),int(data[id+1])
    id +=2
    ditu = [[1001 for _ in range(n+2)] for _ in range(m+2)]
    w_h = [[0 for _ in range(n+2)] for _ in range(m+2)]
    for j in range(1,m+1):
        ditu[j][1:n+1] = list(map(int,data[id:id+n]))
        id +=n
    a,b = int(data[id]),int(data[id+1])
    id +=2
    p = int(data[id])
    id +=1
    def water(q,start):
        while q:
            x,y = q.pop()
            w_h[x][y] = start
            for k in range(4):
                nx = x + move[k][0]
                ny = y + move[k][1]
                if start > ditu[nx][ny] and start >w_h[nx][ny]:
                    q.append([nx, ny])

    for i in range(p):
        q=[(int(data[id]),int(data[id+1]))]
        water(q,ditu[int(data[id])][int(data[id+1])])
        id +=2

    if w_h[a][b] >0:
        print('Yes')
    else:
        print('No')