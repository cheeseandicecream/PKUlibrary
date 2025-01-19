pressed = [[0 for _ in range(8)] for _ in range(7)]
plat = [[0 for _ in range(8)] for _ in range(7)]
for i in range(1,6):
    plat[i][1:7] = map(int,input().split())

cross = [[0,0],[0,-1],[0,1],[1,0],[-1,0]]

import copy

def dfs(first,pressed,plat):
    if len(first) == 6:
        pressed[1][1:7] = first[:]
        for i in range(1,7):
            if first[i-1] == 1:
                for dx,dy in cross:
                    nx,ny = 1+dx,i+dy
                    plat[nx][ny] = abs(plat[nx][ny]-1)
        for x in range(2,6):
            for y in range(1,7):
                if plat[x-1][y] == 1:
                    pressed[x][y] = 1
                    for dx, dy in cross:
                        nx, ny = x + dx, y + dy
                        plat[nx][ny] = abs(plat[nx][ny] - 1)
        if plat[5][1]==plat[5][2]==plat[5][3]==plat[5][4]==plat[5][5]==plat[5][6]==0:
            for ans in pressed[1:6]:
                print(*ans[1:7])
        return
    else:
        for i in range(2):
            l = first[:]
            l.append(i)
            dfs(l,copy.deepcopy(pressed),copy.deepcopy(plat))
        return
l = []
dfs(l,copy.deepcopy(pressed),copy.deepcopy(plat))