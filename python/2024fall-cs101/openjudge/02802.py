from collections import deque
import copy

move = [[0,1],[0,-1],[1,0],[-1,0]]
ans = []
def bfs(matrix,x1,y1,x2,y2,visit):
    q = deque([(x1,y1,0,-1)])
    while q:
        x,y,seq,j = q.popleft()
        visit[y][x] = True
        for i in range(4):
            nx,ny = x+move[i][0],y+move[i][1]
            if matrix[ny][nx] == ' 'and not visit[ny][nx]:
                if j !=i:
                    q.append((nx,ny,seq+1,i))
                else:
                    q.append((nx,ny,seq,i))
            elif nx == x2 and ny == y2:
                if j != i:
                    ans.append(seq+1)
                else:
                    ans.append(seq)
m = 0
while True:
    m+=1
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break
    print(f'Board #{m}:')

    visited = [[False for i in range(w+4)] for j in range(h+4)]
    matrix = [['X' for i in range(w+4)] for j in range(h+4)]
    for i in range(1,h+3):
        matrix[i][1:w+3] = [' ']*(w+2)
    for i in range(2,h+2):
        matrix[i][2:w+2] = input()

    n = 0
    while True:
        n+=1
        x1,y1,x2,y2 = map(int,input().split())
        if x1 == y1 == x2 == y2 ==0:
            break
        ans = []
        v = copy.deepcopy(visited)
        bfs(matrix,x1+1,y1+1,x2+1,y2+1,v)
        if not ans:
            print(f'Pair {n}: impossible.')
        else:
            print(f'Pair {n}: {min(ans)} segments.')
    print()