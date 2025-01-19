# Assignment #10: dp & bfs
Updated 2 GMT+8 Nov 25, 2024
2024 fall, Complied by <mark>同学的姓名、院系</mark>
**说明：**
1）请把每个题目解题思路（可选），源码 Python, 或者 C++（已经在 Codeforces/Openjudge 上 AC），截
图（包含 Accepted ），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用
word）。AC 或者没有 AC，都请标上每个题目大致花费时间。
2）提交时候先提交 pdf 文件，再把 md 或者 doc “ ”文件上传到右侧 作业评论 。Canvas 需要有同学清晰头像、提
交文件有 pdf、"作业评论"区有上传的 md 或者 doc 附件。
3）如果不能在截止前提交作业，请写明原因。
## 1. 题目
### LuoguP1255 数楼梯
dp, bfs, https://www.luogu.com.cn/problem/P1255
思路：
代码：

```python
dp = [0]*5001
dp[1] = 1
dp[2] = 2
for i in range(3,5001):
    dp[i] = dp[i-1] + dp[i-2]
m = int(input())
print(dp[m])
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-11-27 211101.png)

### 27528: 跳台阶
dp, http://cs101.openjudge.cn/practice/27528/
思路：
代码：

```python
dp = [0]*26
dp[0] = 1
dp[1] = 1
for i in range(2,26):
    for j in range(0,i):
        dp[i] +=dp[j]
n = int(input())
print(dp[n])
```
代码运行截图 ==（至少包含有"Accepted"）==

![](D:\Pictures\Screenshots\屏幕截图 2024-11-27 213520.png)

### 474D. Flowers
dp, https://codeforces.com/problemset/problem/474/D
思路：
代码：

```python
t,k = map(int,input().split())

dp = [0]*100001
dp[0] = 1
s = [0]*100001
for i in range(1,100001):
    if i >=k:
        dp[i] = (dp[i-1] + dp[i-k])%(10**9+7)
    else:
        dp[i] = dp[i-1]
    s[i] = (s[i-1] +dp[i])%(10**9+7)
for _ in range(t):
    a,b = map(int,input().split())
    print((s[b]-s[a-1])%(10**9+7))
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-12-01 235010.png)

### LeetCode5.最长回文子串
dp, two pointers, string, https://leetcode.cn/problems/longest-palindromic-
substring/
思路：从整个字符串的长度开始，不断筛选长度越来越小的回文串
代码：

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(a):
            if a == a[::-1]or len(a)==1:
                return True
            return False
        if check(s) or len(s) ==1:
            return s
        for i in range(1,len(s)):
            for j in range(i+1):
                if check(s[j:len(s)+j-i]):
                    return s[j:len(s)+j-i]
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-12-01 225929.png)

### 12029: 水淹七军
bfs, dfs, http://cs101.openjudge.cn/practice/12029/
思路：
代码：

```python
import sys
from collections import deque
data = sys.stdin.read().split()

move = [[1,0],[0,1],[-1,0],[0,-1]]

k = int(data[0])
id = 1
for _ in range(k):
    m,n = int(data[id]),int(data[id+1])
    id +=2
    ditu = [[1001 for _ in range(n+2)] for _ in range(m+2)]
    w_h = [[0 for _ in range(n+2)] for _ in range(m+2)]
    for j in range(1,m+1):
        ditu[j][1:n+1] = list(map(int,data[id:id+n]))
        id +=n
    a,b = int(data[id]),int(data[id+1])
    id +=2
    p = int(data[id])
    id +=1
    def water(q,start):
        while q:
            x,y = q.pop()
            w_h[x][y] = start
            for k in range(4):
                nx = x + move[k][0]
                ny = y + move[k][1]
                if start > ditu[nx][ny] and start >w_h[nx][ny]:
                    q.append([nx, ny])

    for i in range(p):
        q=[(int(data[id]),int(data[id+1]))]
        water(q,ditu[int(data[id])][int(data[id+1])])
        id +=2

    if w_h[a][b] >0:
        print('Yes')
    else:
        print('No')
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-12-02 115352.png)

### 02802: 小游戏
bfs, http://cs101.openjudge.cn/practice/02802/
思路：
代码：

```python
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
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-12-02 172057.png)

## 2. 学习总结和收获
<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概 2024fall ”每日选做 、CF、LeetCode、洛谷
等网站题目。</mark>

这次作业的题目感觉思路并不难想，就是因为各种原因出现类似runtime error的小错误，看来也是平时练习少导致的。

最近刚刚感冒，这周周末主要就是生病了，我打算下周补一补每日选做，保持手感。

顺带一提，我感觉现在的AI并不擅长给代码挑错，很多时候我遇到一些小问题AI发现不了。