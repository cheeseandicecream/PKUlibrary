# Assignment #8: 田忌赛马来了
Updated 1021 GMT+8 Nov 12, 2024
2024 fall, Complied by <mark>同学的姓名、院系</mark>
**说明：**
1）请把每个题目解题思路（可选），源码 Python, 或者 C++（已经在 Codeforces/Openjudge 上 AC），截
图（包含 Accepted ），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用
word）。AC 或者没有 AC，都请标上每个题目大致花费时间。
2）提交时候先提交 pdf 文件，再把 md 或者 doc “ ”文件上传到右侧 作业评论 。Canvas 需要有同学清晰头像、提
交文件有 pdf、"作业评论"区有上传的 md 或者 doc 附件。
3）如果不能在截止前提交作业，请写明原因。
## 1. 题目
### 12558: 岛屿周⻓
matices, http://cs101.openjudge.cn/practice/12558/
思路：
代码：

```python
n,m = map(int,input().split())
d=[[0]*(m+2)]
for i in range(n):
    d.append([0]+list(map(int,input().split()))+[0])
d.append([0]*(m+2))
ans = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if d[i][j]==1:
            ans +=4 - d[i+1][j]-d[i-1][j]-d[i][j+1]-d[i][j-1]
print(ans)
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-11-15 111154.png)

### LeetCode54.螺旋矩阵
matrice, https://leetcode.cn/problems/spiral-matrix/
与 OJ 这个题目一样的 18106: 螺旋矩阵，http://cs101.openjudge.cn/practice/18106
思路：设置x,y指标，让指标旋转着选取列表元素
代码：

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        n = len(matrix)
        m = len(matrix[0])
        def spin(matrix,ans,x,y):
            for i in range(x,m-x):
                ans.append(matrix[y][i])
            if y >n//2-1:
                return ans

            for j in range(y+1,n-y):
                ans.append(matrix[j][m-x-1])
            if x>m//2-1:
                return ans

            for i in range(m-x-2,x-1,-1):
                ans.append(matrix[n-y-1][i])
            if y==n/2-1:
                return ans

            for j in range(n-y-2,y,-1):
                ans.append(matrix[j][x])
            if x == m/2-1:
                return ans
            
            spin(matrix,ans,x+1,y+1)
        spin(matrix, ans,0,0)
        return ans
```
代码运行截图 ==（至少包含有"Accepted"）==

![](D:\Pictures\Screenshots\屏幕截图 2024-11-15 162502.png)

### 04133:垃圾炸弹
matrices, http://cs101.openjudge.cn/practice/04133/
思路：
代码：

```python
dp = [[0]*1025 for i in range(1025)]

d = int(input())
n = int(input())
ans = 0
m=0
for _ in range(n):
    x,y,i = map(int,input().split())
    for a in range(-d,d+1):
        for b in range(-d,d+1):
            if x+a>=1025 or x+a<0 or y+b>=1025 or y+b<0:
                continue
            dp[x+a][y+b] +=i
for i in range(1025):
    for j in range(1025):
        ans = max(ans,dp[i][j])
for i in range(1025):
    for j in range(1025):
        if ans == dp[i][j]:
            m+=1
print(f'{m} {ans}')
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-11-15 165009.png)

### LeetCode376.摆动序列
greedy, dp, https://leetcode.cn/problems/wiggle-subsequence/
与 OJ 这个题目一样的，26976:摆动序列, http://cs101.openjudge.cn/routine/26976/
思路：当三个排列在一起的数字不能组成摆动序列的时候，这意味着中间那个数字的大小在相邻两个之间，
代码：

```python
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        elif len(nums)==2:
            if nums[0]==nums[1]:
                return 1
            return 2
        i = 1
        while i < len(nums) -1:
            if nums[i-1]>=nums[i]>=nums[i+1] or nums[i-1]<=nums[i]<=nums[i+1] :
                del nums[i]
                continue
            i+=1
        if nums[0]==nums[1]:
                return 1
        return len(nums)
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-11-15 202203.png)

### CF455A: Boredom
dp, 1500, https://codeforces.com/contest/455/problem/A
思路：用一个表格的第i个元素表示如果选择数字i会得到的分数，再在这个基础上跨越一个或两个数字计算得分
代码：

```python
n = int(input())
nums = list(map(int, input().split()))
m = max(nums)
dp = [0] * (m + 1)
for i in range(n):
    dp[nums[i]]+=nums[i]
dp[2]+=dp[0]
for i in range(3,m+1):
    dp[i] += max(dp[i-3],dp[i-2])
print(max(dp))
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-11-16 000025.png)

### 02287: Tian Ji -- The Horse Racing
greedy, dfs http://cs101.openjudge.cn/practice/02287
思路：自己的思路最后发现还是有问题，采用了题解中的双指针做法
代码：

```python
while True:
    n = int(input())
    if n == 0:
        break
    T_horses = list(map(int, input().split()))
    K_horses = list(map(int, input().split()))
    T_horses.sort()
    K_horses.sort()
    ans = 0
    lT = 0 ; rT = n-1
    lK = 0 ; rK = n-1
    while lT<=rT:
        if T_horses[lT]>K_horses[lK]:
            ans += 1
            lT +=1 ; lK += 1
        elif T_horses[rT]>K_horses[rK]:
            ans += 1
            rT -=1 ; rK -= 1
        else:
            if T_horses[lT]<K_horses[rK]:
                ans -=1
            lT +=1 ; rK -= 1
    print(ans*200)
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-11-16 162418.png)

## 2. 学习总结和收获
<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概 2024fall ”每日选做 、CF、LeetCode、洛谷
等网站题目。</mark>

期末考试终于结束了，现在每天都会抽出一定的时间做几道每日选做，感觉不断学习解答中巧妙的思路非常有帮助。

田忌赛马那道题我思考了三四个小时，我考虑的思路是单独讨论平局的情况，结果总是不断发现反例，看了解答发现其实找到平局和败局不一样之处（即大马之间的胜负）才是破局的关键。感觉看了解答之后会发现越是简洁的思路越容易纠错，越少反例。

