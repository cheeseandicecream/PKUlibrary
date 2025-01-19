import heapq
from collections import defaultdict


def bfs(n,m):
    q = []
    visited = defaultdict(int)
    heapq.heapify(q)
    heapq.heappush(q,[0,'',n])
    visited[n] = 1
    while q:
        k,word,p = heapq.heappop(q)
        if p == m :
            return [k,word]
        if visited[3*p] == 0:
            heapq.heappush(q,[k+1,word+'H',3*p])
            visited[3*p] = 1
        if visited[p//2] == 0:
            heapq.heappush(q,[k+1,word+'O',p//2])
            visited[p//2] = 1


while True:
    n,m = map(int,input().split())
    if n == m ==0:
        break
    ans = bfs(n,m)
    print(ans[0])
    print(ans[1])