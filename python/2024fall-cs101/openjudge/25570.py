from collections import deque
from copy import deepcopy

n = int(input())
matrix = deque()
for _ in range(n):
    matrix.append(deque(map(int, input().split())))
ans = 0

def pick(i,m):
    global ans
    if i ==1:
        ans = max(ans,m[0][0])
        return
    elif i ==2:
        k = 0
        k += sum(m.popleft())
        k += sum(m.pop())
        ans = max(ans, k)
        return
    k = 0
    k+= sum(m.popleft())
    k+= sum(m.pop())
    for j in range(i-2):
        k+= m[j].popleft()
        k+= m[j].pop()
    ans = max(ans, k)
    pick(i-2,deepcopy(m))

pick(n,matrix)
print(ans)