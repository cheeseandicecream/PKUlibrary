# Assignment #C: 五味杂陈
Updated 1148 GMT+8 Dec 10, 2024
2024 fall, Complied by <mark>同学的姓名、院系</mark>
**说明：**
1）请把每个题目解题思路（可选），源码 Python, 或者 C++（已经在 Codeforces/Openjudge 上 AC），截
图（包含 Accepted ），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用
word）。AC 或者没有 AC，都请标上每个题目大致花费时间。
2）提交时候先提交 pdf 文件，再把 md 或者 doc “ ”文件上传到右侧 作业评论 。Canvas 需要有同学清晰头像、提
交文件有 pdf、"作业评论"区有上传的 md 或者 doc 附件。
3）如果不能在截止前提交作业，请写明原因。
## 1. 题目
### 1115. 取石子游戏
dfs, https://www.acwing.com/problem/content/description/1117/
思路：让两堆石子来回减，直到可以直接判断胜负，根据此时的棋手确定胜负
代码：

```python
def pick(a,b,i):
    if a %b ==0 :
        return i
    if a >=2*b :
        return i
    return pick(b,a-b,i+1)

while True:
    a,b = map(int,input().split())
    if a == b ==0:
        break
    if a < b:
        a,b = b,a
    if pick(a,b,0) % 2 ==0:
        print('win')
    else:
        print('lose')
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-12-12 171055.png)

### 25570: 洋葱
Matrices, http://cs101.openjudge.cn/practice/25570
思路：用递归一层层剥洋葱，
代码：

```python
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
```
代码运行截图 ==（至少包含有"Accepted"）==

![](D:\Pictures\Screenshots\屏幕截图 2024-12-15 000239.png)

### 1526C1. Potions(Easy Version)
greedy, dp, data structures, brute force, *1500, https://codeforces.com/problemset/problem/1526/C1
思路：学习了题解贪心的后悔算法，真巧妙
代码：

```python
import heapq

n = int(input())
potions = list(map(int, input().split()))

def drink(potions):
    drinked = []
    h = 0
    for potion in potions:
        heapq.heappush(drinked,potion)
        h +=potion
        if h <0:
            if drinked:
                h -=heapq.heappop(drinked)
    return len(drinked)
print(drink(potions))
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-12-15 221732.png)

### 22067: 快速堆猪
辅助栈，http://cs101.openjudge.cn/practice/22067/
思路：这道题的思路很有贪心的感觉，如果发现只要再用一个列表储存最小值就很简单，但感觉我很难想到
代码：

```python
import sys

data = sys.stdin.read().splitlines()
pigs = []
m_pigs = []

def push(x,pigs,m_pigs):
    pigs.append(x)
    if not m_pigs:
        m_pigs.append(x)
    elif x<=m_pigs[-1]:
        m_pigs.append(x)

for line in data:
    if line =="min":
        if m_pigs:
            print(m_pigs[-1])
    elif line =="pop":
        if pigs:
            x=pigs.pop()
            if x == m_pigs[-1]:
                m_pigs.pop()
    else:
        a,b = line.split()
        push(int(b),pigs,m_pigs)
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-12-15 221707.png)

### 20106: 走山路
Dijkstra, http://cs101.openjudge.cn/practice/20106/
思路：看了题解才明白，这是一个广义的bfs
代码：

```python
import heapq

m,n,p = map(int,input().split())
plat = [['#' for _ in range(n+2)] for _ in range(m+2)]
for i in range(1,m+1):
    plat[i][1:n+1] = input().split()
move = [[0,1],[0,-1],[1,0],[-1,0]]
ans = float('inf')

def climb(x1,y1,x2,y2,plat,dp):
    if plat[x_1][y_1] == '#'or plat[x_2][y_2] == '#':
        return 'NO'
    heap = [(0,x1,y1)]
    found = False

    while heap:
        cost,x,y = heapq.heappop(heap)
        if x == x2 and y == y2:
            found = True
            return cost
        for dx,dy in move:
            nx,ny = x + dx,y + dy
            if plat[nx][ny] != '#':
                n_cost = cost + abs(int(plat[nx][ny])-int(plat[x][y]))
                if n_cost < dp[nx][ny]:
                    heapq.heappush(heap,(n_cost,nx,ny))
                    dp[nx][ny] = n_cost
    if not found:
        return 'NO'

for _ in range(p):
    ans = float('inf')
    dp = [[float('inf') for _ in range(n+2)] for _ in range(m+2)]
    x_1,y_1,x_2,y_2 = map(int,input().split())
    x_1 +=1; y_1+=1; x_2+=1; y_2+=1
    print(climb(x_1,y_1,x_2,y_2,plat,dp))
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-12-16 111404.png)

### 04129: 变换的迷宫
bfs, http://cs101.openjudge.cn/practice/04129/
思路：因为迷宫以k为周期，所以如果在t+mk(m为正整数)时间访问在t时间以已经访问过的点，就可以做剪枝，其余是一个普通的bfs
代码：

```python
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
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-12-16 123008.png)

## 2. 学习总结和收获
<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概 2024fall ”每日选做 、CF、LeetCode、洛谷
等网站题目。</mark>

感觉自己实力还是不太行，这次作业的很多题目我都有和题解类似的思路，但找不到合适的实现方法，就像国足，临门一脚踢不进去。我想应该还是见过的题目太少的问题，缺乏积累。
