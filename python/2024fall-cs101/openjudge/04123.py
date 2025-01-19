move = [[1,2],[2,1],[2,-1],[-1,2],[-2,1],[1,-2],[-1,-2],[-2,-1]]

step = 0

def jump(mapp,x,y,k,w):
    global step
    if mapp[x][y] ==1:
        if k ==w:
            step +=1
        return
    else:
        mapp[x][y] = 1
        for i in range(8):
            nx = x +move[i][0]
            ny = y +move[i][1]
            jump(mapp,nx,ny,k+1,w)
        mapp[x][y] = 0

t = int(input())
for _ in range(t):
    n,m,x,y = map(int,input().split())
    mapp = [[1 for _ in range(m+4)] for _ in range(n+4)]
    for i in range(2,n+2):
        mapp[i][2:m+2] = [0 for _ in range(m)]
    step = 0
    jump(mapp,x+2,y+2,0,n*m)
    print(step//8)
