m,n = map(int,input().split())
mapp = [[2 for _ in range(n+2)] for _ in range(m+2)]
for i in range(1,m+1):
    mapp[i][1:n+1] = map(int,input().split())

move = [[1,0],[-1,0],[0,1],[0,-1]]

steps = []
def search(mapp,x,y,step):
    if mapp[x][y] == 2:
        return
    elif mapp[x][y] == 1:
        steps.append(step)
        return
    elif mapp[x][y] == 0:
        step +=1
        mapp[x][y] = 2
        for i in range(4):
            nx = x+move[i][0]
            ny = y+move[i][1]
            search(mapp,nx,ny,step)
        mapp[x][y] = 0

if mapp[1][1] == 1:
    print(0)
else:
    search(mapp, 1, 1, 0)
    if not steps:
        print('NO')
    else:
        print(min(steps))
