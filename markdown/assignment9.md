# Assignment #9: dfs, bfs, & dp
Updated 2107 GMT+8 Nov 19, 2024
2024 fall, Complied by <mark>同学的姓名、院系</mark>
**说明：**
1）请把每个题目解题思路（可选），源码 Python, 或者 C++（已经在 Codeforces/Openjudge 上 AC），截
图（包含 Accepted ），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用
word）。AC 或者没有 AC，都请标上每个题目大致花费时间。
2）提交时候先提交 pdf 文件，再把 md 或者 doc “ ”文件上传到右侧 作业评论 。Canvas 需要有同学清晰头像、提
交文件有 pdf、"作业评论"区有上传的 md 或者 doc 附件。
3）如果不能在截止前提交作业，请写明原因。
## 1. 题目
### 18160: 最大连通域面积
dfs similar, http://cs101.openjudge.cn/practice/18160
思路：
代码：

```python
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
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-11-23 145950.png)

用时：40min

### 19930: 寻宝

bfs, http://cs101.openjudge.cn/practice/19930
思路：
代码：

```python
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
```
代码运行截图 ==（至少包含有"Accepted"）==

用时：24min

### 04123: 马走日
dfs, http://cs101.openjudge.cn/practice/04123
思路：先加两层保护圈，当搜索程序走到走过的位置上时判断此时的步数是否等于棋盘上最开始的空位数，如果等于，说明此时马已经走遍了棋盘，step+=1，但考虑到我是在最后马走完棋盘后再多一步才结算，结果会算成8倍，最后再除去就可以了。
代码：

```python
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
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-11-23 162553.png)

### sy316: 矩阵最大权值路径
dfs, https://sunnywhy.com/sfbj/8/1/316
思路：按照深度搜索写的代码，但这里最大的坑点是列表在迭代的时候有个浅拷贝的问题。
代码：

```python
move = [[0,1],[1,0],[0,-1],[-1,0]]

n,m = map(int,input().split())
matrix = [[-101 for i in range(m+2)] for j in range(n+2)]
for i in range(1,n+1):
    matrix[i][1:m+1] = map(int,input().split())
key = float('-inf')
ans = []

def search(matrix,x,y,k,steps):
    global key
    global ans
    if matrix[x][y] == -101:
        return
    steps.append([x, y])
    k += matrix[x][y]
    if x ==n and y==m:
        if k >key :
            key = k
            ans = steps.copy()
        return
    a = matrix[x][y]
    matrix[x][y] = -101
    for i in range(4):
        nx = x+move[i][0]
        ny = y+move[i][1]
        search(matrix,nx,ny,k,steps[:])
    matrix[x][y] = a

search(matrix,1,1,0,[])
for j in ans :
    print(*j)
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-11-23 182844.png)

### LeetCode62.不同路径
dp, https://leetcode.cn/problems/unique-paths/
思路：
代码：

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        dp[1][1] = 1
        for i in range(1, n+1):
            for j in range(1, m+1):
                if i == j ==1:
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[n][m]
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-11-23 184248.png)

### sy358: 受到祝福的平方
dfs, dp, https://sunnywhy.com/sfbj/8/3/539
思路：做这道题的时候我一直在思考贪心策略，最后才发现没法解决的反例，看了题解才知道要用dfs。
代码：

```python
squares = []
i = 1
while i**2 <=10**9:
    squares.append(i**2)
    i +=1

a = list(map(int,str(input())))

def dfs(k,a):
    if k == len(a):
        return True

    num = 0
    for i in range(k,len(a)):
        num = num*10 + a[i]
        if num in squares:
            if dfs(i+1,a):
                return True
    return False

if dfs(0,a):
    print('Yes')
else:
    print('No')

```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-11-23 213937.png)

## 2. 学习总结和收获
<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概 2024fall ”每日选做 、CF、LeetCode、洛谷
等网站题目。</mark>

期中考试终于结束了，我这周抽空把每周发的讲义看了一下，感觉收获很大。我发现现在越来越多的算法是自己很难凭空想出来的，只有接触过一些相关的例子才好举一反三。

感觉dp和dfs的难点很奇怪，发现问题可以这样解决后代码并不难写，但难在发现问题适合采用这样的解法。