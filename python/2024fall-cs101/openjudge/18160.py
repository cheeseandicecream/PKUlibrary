m = int(input())
for _ in range(m):
    N,M = map(int,input().split())
    da = [['.'for _ in range(M+2)] for _ in range(N+2)]
    v = [[False for _ in range(M+2)] for _ in range(N+2)]

    for i in range(1,N+1):
        da[i][1:M+1] = input()

    step = [[-1,-1],[-1,0],[0,-1],[-1,1],[0,1],[1,1],[1,0],[1,-1]]

    ans = 0
    e = 0

    def search(v,da,x,y):
        global ans
        if da[x][y] == '.':
            return
        if v[x][y]:
            return
        ans += 1
        v[x][y] = True
        for j in range(8):
            nx = x+step[j][0]
            ny = y+step[j][1]
            search(v,da,nx,ny)

    for x in range(1,N+1):
        for y in range(1,M+1):
            search(v,da,x,y)
            e = max(e,ans)
            ans = 0

    print(e)

