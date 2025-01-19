# Assignment #D: 十全十美
Updated 1254 GMT+8 Dec 17, 2024
2024 fall, Complied by <mark>同学的姓名、院系</mark>
**说明：**
1）请把每个题目解题思路（可选），源码 Python, 或者 C++（已经在 Codeforces/Openjudge 上 AC），截
图（包含 Accepted ），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用
word）。AC 或者没有 AC，都请标上每个题目大致花费时间。
2）提交时候先提交 pdf 文件，再把 md 或者 doc “ ”文件上传到右侧 作业评论 。Canvas 需要有同学清晰头像、提
交文件有 pdf、"作业评论"区有上传的 md 或者 doc 附件。
3）如果不能在截止前提交作业，请写明原因。
## 1. 题目
### 02692: 假币问题
brute force, http://cs101.openjudge.cn/practice/02692
思路：
代码：

```python
n = int(input())
coin_w = ['heavy','light']
for _ in range(n):
    fake = {}
    true = []
    for i in range(3):
        inp = input().split()
        if inp[2] == 'even':
            for j in inp[0]+inp[1]:
                if j not in true:
                    true.append(j)
        elif inp[2] == 'up':
            for j in inp[0]:
                if fake.get(j) ==1:
                    true.append(j)
                    continue
                fake[j] = 0
            for j in inp[1]:
                if fake.get(j) ==0:
                    true.append(j)
                    continue
                fake[j] = 1
        elif inp[2] == 'down':
            for j in inp[0]:
                if fake.get(j) ==0:
                    true.append(j)
                    continue
                fake[j] = 1
            for j in inp[1]:
                if fake.get(j) ==1:
                    true.append(j)
                    continue
                fake[j] = 0
    for k in fake:
        if k not in true:
            print(f'{k} is the counterfeit coin and it is {coin_w[fake[k]]}.')
            break
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-12-19 175538.png)

### 01088: 滑雪
dp, dfs similar, http://cs101.openjudge.cn/practice/01088
思路：同时采用了bfs和dp的思路，每个较矮的高度可以让旁边的峰变为其步数数字加一，但这个思路必须从最小的峰开始
代码：

```python
import heapq

r,c = map(int,input().split())
visited = {(x,y):0 for x in range(r) for y in range(c)}
plat = [list(map(int,input().split())) for _ in range(r)]
move = [[0,1],[1,0],[-1,0],[0,-1]]
ans = 0
q = []
heapq.heapify(q)
for i in range(r):
    for j in range(c):
        heapq.heappush(q,(plat[i][j],i,j)  )
for _ in range(r*c):
    h,x,y = heapq.heappop(q)
    for dx,dy in move:
        nx,ny = x+dx,y+dy
        if 0<=nx<r and 0<=ny<c:
            if visited[nx,ny]<visited[x,y]+1 and h<plat[nx][ny]:
                visited[nx,ny] = visited[x,y]+1
                ans = max(ans,visited[nx,ny])
print(ans+1)
```
代码运行截图 ==（至少包含有"Accepted"）==

![](D:\Pictures\Screenshots\屏幕截图 2024-12-19 175426.png)

### 25572: 螃蟹采蘑菇
bfs, dfs, http://cs101.openjudge.cn/practice/25572/
思路：先用dfs找到螃蟹，再用bfs找到蘑菇
代码：

```python
from collections import deque

n = int(input())
plat = [[1 for _ in range(n+2)] for _ in range(n+2)]
for i in range(1,n+1):
    plat[i][1:n+1] = map(int, input().split())
move = [[0,1],[0,-1],[1,0],[-1,0]]

def dfs(plat,n):
    out = []
    for i in range(1,n+1):
        for j in range(1,n+1):
            if plat[i][j] == 5:
                out.append((i,j))
    return out

def bfs(l):
    q = deque()
    x1,y1 = l[0]
    x2,y2 = l[1]
    q.append((x1,y1,x2,y2))
    while q:
        x1, y1, x2, y2 = q.popleft()
        if plat[x1][y1] == 9 or plat[x2][y2] == 9:
            return True
        for dx,dy in move:
            nx1,ny1,nx2,ny2 = x1 + dx,y1 + dy,x2 + dx,y2 + dy
            if plat[nx1][ny1] !=1 and plat[nx2][ny2]!=1:
                q.append((nx1,ny1,nx2,ny2))
        plat[x1][y1],plat[x2][y2] = 1,1
    return False

if bfs(dfs(plat,n)):
    print('yes')
else:
    print('no')
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-12-19 182408.png)

### 27373: 最大整数
dp, http://cs101.openjudge.cn/practice/27373/
思路：看到dp的提示大概就知道要用数字位数作动态规划了，再回忆一下字典序排列的做法就行了
代码：

```python
m = int(input())
n = int(input())
numbers = input().split()
l = []
for number in numbers:
    if len(number) <=m:
        k = m - len(number)
        l.append( (number+f'{number[0]}'*k ,number) )
l.sort(reverse=True)
dp = ['']*(m+1)
for j in range(len(l)):
    number = l[j][1]
    f = len(number)
    for i in range(m-f,-1,-1):
        ou = dp[i] + number
        if not dp[i+f] or int(ou) > int(dp[i+f]):
            dp[i+f] = ou

print(int(dp[m]))
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>
### 02811: 熄灯问题
brute force, http://cs101.openjudge.cn/practice/02811
思路：看了题解才明白，这就纯粹穷举题，不过一行一行穷举的思路还挺妙的
代码：

```python
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
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-12-22 184735.png)

### 08210: 河中跳房子
binary search, greedy, http://cs101.openjudge.cn/practice/08210/
思路：
代码：

```python
ans = 0
l,n,m = map(int,input().split())
rocks = [0]*(n+2)
rocks[n+1] = l
for i in range(1,n+1):
    rocks[i] = int(input())

def jump(dp,m,n,l):
    now = 0
    k =0
    for i in range(1,n+2):
        if dp[i]-now <l:
            k+=1
        else:
            now = dp[i]
    if k>m:
        return True
    else:
        return False

min1 = 0
max1 = l+1
while max1>min1:
    mid = (min1+max1)//2
    if jump(rocks,m,n,mid):
        max1 = mid
    else:
        ans = mid
        min1 = mid+1
print(ans)
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-12-22 184653.png)

## 2. 学习总结和收获
<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概 2024fall ”每日选做 、CF、LeetCode、洛谷
等网站题目。</mark>

好忙啊啊啊。

这次的作业后面两道自己没做出来，对我来说是新的思路，看来还是题目见少了（捂脸）。我打算下周把历年的期末题目做一下。
