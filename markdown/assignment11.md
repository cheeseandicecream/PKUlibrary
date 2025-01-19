# Assignment #B: Dec Mock Exam 大雪前一天
Updated 1649 GMT+8 Dec 5, 2024
2024 fall, Complied by <mark>同学的姓名、院系</mark>
**说明：**
1 ）月考： AC1<mark>（请改为同学的通过数）</mark> “ ”。考试题目都在 题库（包括计概、数算题目） 里面，
按照数字题号能找到，可以重新提交。作业中提交自己最满意版本的代码和截图。
2）请把每个题目解题思路（可选），源码 Python, 或者 C++（已经在 Codeforces/Openjudge 上 AC），截
图（包含 Accepted ），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用
word）。AC 或者没有 AC，都请标上每个题目大致花费时间。
3）提交时候先提交 pdf 文件，再把 md 或者 doc “ ”文件上传到右侧 作业评论 。Canvas 需要有同学清晰头像、提
交文件有 pdf、"作业评论"区有上传的 md 或者 doc 附件。
4）如果不能在截止前提交作业，请写明原因。

## 1. 题目
### E22548: 机智的股民老张
http://cs101.openjudge.cn/practice/22548/
思路：建立一个dp列表，其中dp[i]表示第i天及以后的最高股价，从i=len(a)反向建立列表。
代码：

```python
a = list(map(int,input().split()))
ans = 0
n = len(a)
dp = [0]*n
dp[n-1] = a[n-1]
for i in range(n-2,-1,-1):
    dp[i] = max(dp[i+1],a[i])
for i in range(len(a)):
        if dp[i]-a[i]>ans:
            ans = dp[i]-a[i]
print(ans)
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-12-08 212711.png)

### M28701: 炸鸡排
greedy, http://cs101.openjudge.cn/practice/28701/
思路：如果有鸡扒一直在锅里，那就直接刨除这块鸡扒，假装少一个锅。
代码：

```python
n,k = map(int,input().split())
chickens = list(map(int,input().split()))
s = sum(chickens)
chickens.sort(reverse=True)
for i in range(n):
    if chickens[i] <=s/k:
        break
    k -=1
    s -= chickens[i]
ans = f'{s/k:.3f}'
print(ans)
```
代码运行截图 ==（至少包含有"Accepted"）==

![](D:\Pictures\Screenshots\屏幕截图 2024-12-08 214101.png)

### M20744: 土豪购物
dp, http://cs101.openjudge.cn/practice/20744/
思路：
代码：学习题解中的思路，太妙了

```python
items = list(map(int, input().split(',')))
n = len(items)
dp1 = [0]*n
dp2 = [0]*n
dp1[0] = items[0]
dp2[0] = items[0]
for i in range(1,n):
    dp1[i] = max(dp1[i-1]+items[i], items[i])
    dp2[i] = max(dp1[i-1], items[i],dp2[i-1]+items[i])
print(max(dp2))
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-12-08 224732.png)

### T25561: 2022 决战双十一
brute force, dfs, http://cs101.openjudge.cn/practice/25561/
思路：
代码：

```python
result = float("inf")
n, m = map(int, input().split())
store_prices = [input().split() for _ in range(n)]
you= [input().split() for _ in range(m)]
la=[0]*m
def dfs(i,sum1):
    global result
    if i==n:
        jian=0
        for i2 in range(m):
            store_j=0
            for k in you[i2]:
                a,b=map(int,k.split('-'))
                if la[i2]>=a:
                    store_j=max(store_j,b)
            jian+=store_j
        result=min(result,sum1-(sum1//300)*50-jian)
        return
    for i1 in store_prices[i]:
        idx,p=map(int,i1.split(':'))
        la[idx-1]+=p
        dfs(i+1,sum1+p)
        la[idx-1]-=p
dfs(0,0)
print(result)
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-12-09 221343.png)

### T20741: 两座孤岛最短距离
dfs, bfs, http://cs101.openjudge.cn/practice/20741/
思路：
代码：

```python
from collections import deque

def dfs(x, y, grid, n, queue, directions):
    """ Mark the connected component starting from (x, y) as visited using DFS. """
    grid[x][y] = 2  # Mark as visited
    queue.append((x, y))
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
            dfs(nx, ny, grid, n, queue, directions)

def bfs(grid, n, queue, directions):
    """ Perform BFS to find the shortest path to another component. """
    distance = 0
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    if grid[nx][ny] == 1:
                        return distance
                    elif grid[nx][ny] == 0:
                        grid[nx][ny] = 2  # Mark as visited
                        queue.append((nx, ny))
        distance += 1
    return distance

def main():
    n = int(input())
    grid = [list(map(int, input())) for _ in range(n)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque()

    # Start DFS from the first '1' found and use BFS from there
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                dfs(i, j, grid, n, queue, directions)
                return bfs(grid, n, queue, directions)

if __name__ == "__main__":
    print(main())
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-12-09 220713.png)

### T28776: 国王游戏
greedy, http://cs101.openjudge.cn/practice/28776
思路：最后一个大臣得到的金币等于所有人左手的数字相乘除以他左右手数字相乘，所以只要找到左右手数字相乘最大的那个大臣即可。
代码：

```python
n = int(input())
a,b = map(int,input().split())
l = a
lr = []
for i in range(n):
    x,y = map(int,input().split())
    lr.append(x*y)
    l = l*x
lr.sort(reverse=True)
print(l//lr[0])
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-12-08 215004.png)

## 2. 学习总结和收获
<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概 2024fall ”每日选做 、CF、LeetCode、洛谷
等网站题目。</mark>

这套题目对我来说就是降维打击，好多算法优化的思路都没见过，但仔细跟着题解学习一遍收获还是挺大的，但这套题目对我的自信心还是有明显的打击（捂脸）

无论是双dp，高阶的dfs算法都让人感觉特别巧妙，但我很怀疑自己能不能在考场上想出来。这套卷子只AC1，要是期末考试这样不知道会不会就挂科了。

接下来我会好好努力的，争取最后别剃光头。
