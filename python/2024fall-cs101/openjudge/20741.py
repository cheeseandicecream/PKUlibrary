from collections import deque
directions = [[0,1],[0,-1],[-1,0],[1,0]]

def dfs(n,grid,directions,queue,x,y):
    grid[x][y]=2
    queue.append((x,y))
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<n:
            if grid[nx][ny]==1:
                dfs(n,grid,directions,queue,nx,ny)

def bfs(n,grid,directions,queue):
    distance = 0
    while queue:
        for _ in range(len(queue)):
            x,y=queue.popleft()
            for dx,dy in directions:
                nx,ny=x+dx,y+dy
                if 0<=nx<n and 0<=ny<n:
                    if grid[nx][ny]==1:
                        return distance
                    elif grid[nx][ny]==0:
                        grid[nx][ny]=2
                        queue.append((nx,ny))
        distance += 1
    return distance

def main():
    n = int(input())
    grid = [list(map(int, input())) for _ in range(n)]
    queue = deque()

    for i in range(n):
        for j in range(n):
            dfs(n,grid,directions,queue,i,j)
            return bfs(n,grid,directions,queue)

if __name__ == '__main__':
    print(main())