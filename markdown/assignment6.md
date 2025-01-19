# Assignment #6: Recursion and DP
Updated 2201 GMT+8 Oct 29, 2024
2024 fall, Complied by <mark>同学的姓名、院系</mark>
**说明：**
1）请把每个题目解题思路（可选），源码 Python, 或者 C++（已经在 Codeforces/Openjudge 上 AC），截
图（包含 Accepted ），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用
word）。AC 或者没有 AC，都请标上每个题目大致花费时间。
3）提交时候先提交 pdf 文件，再把 md 或者 doc “ ”文件上传到右侧 作业评论 。Canvas 需要有同学清晰头像、提
交文件有 pdf、"作业评论"区有上传的 md 或者 doc 附件。
4）如果不能在截止前提交作业，请写明原因。
## 1. 题目
### sy119: 汉诺塔
recursion, https://sunnywhy.com/sfbj/4/3/119
思路：可以将一次n块板的搬运可以分解为两次n-1的搬运
代码：

```python
def move(m,a,b,c):
    if m ==0:
        return
    move(m-1,a,c,b)
    print(f'{a}->{c}')
    move(m-1,b,a,c)

n = int(input())
print(2**n-1)
move(n,'A','B','C')
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-11-01 141801.png)

### sy132: 全排列 I
recursion, https://sunnywhy.com/sfbj/4/3/132
思路：一个n个数字的全排列可以分解为n个n-1个数字的全排列——通过在原来的列表中将一个数字提到最前面实现。由此类推，就可以把n个数字的全排列减少到1个数字的全排列，最后输出
代码：

```python
n = int(input())
l = [i for i in range(1,n+1)]
t = []

def make(i,j):
    if len(i)==0:
        print(*j)
    for k in range(len(i)):
        m = i[:]
        a = j[:]
        a.append(m.pop(k))
        make(m,a)

make(l,t)
```
代码运行截图 ==（至少包含有"Accepted"）==

![](D:\Pictures\Screenshots\屏幕截图 2024-11-01 154900.png)

### 02945: 拦截导弹
dp, http://cs101.openjudge.cn/2024fallroutine/02945
思路：定义一个函数，其用处是计算如果先拦截第i个导弹，最多能拦截的导弹数，让这个函数和后面高度更低的导弹的函数递归。其中，如果没有后续导弹可以拦截，则函数值为1.
代码：

```python
k = int(input())
missiles = list(map(int, input().split()))

def compete(i,n,l):
    m = 0
    for j in range(i+1,n):
        if l[i]>=l[j]:
            m = max(m,compete(j,n,l)+1)
    if m ==0:
        return 1
    return m

ans = 0
for i in range(k):
    ans = max(ans, compete(i,k,missiles))
print(ans)
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-11-01 193751.png)

### 23421: 小偷背包
dp, http://cs101.openjudge.cn/practice/23421
思路：
代码：

```python
N,B = map(int,input().split())
prices = list(map(int,input().split()))
weights = list(map(int,input().split()))

dp = [0]*(B+1)
for i in range(N):
    for j in range(B,weights[i]-1,-1):
        dp[j]= max(dp[j],dp[j-weights[i]]+prices[i])
print(dp[-1])
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-11-01 234259.png)

### 02754: 八皇后
dfs and similar, http://cs101.openjudge.cn/practice/02754
思路：枚举所有可能的情况，然后检查是否满足斜线不相交
代码：

```python
n = int(input())

def check(l):
    for i in range(8):
        for j in range(i+1,8):
            if abs(l[i] - l[j]) == abs(i-j):
                return False
    return True

ans = []

for i in range(1,9):
    for j in [x for x in range(1,9) if x !=i]:
        for k in [x for x in range(1,9) if x not in {i,j}]:
            for m in [x for x in range(1,9) if x not in {i,j,k}]:
                for q in [x for x in range(1,9) if x not in {i, j,k,m}]:
                    for w in [x for x in range(1,9) if x not in {i, j, k, m,q}]:
                        for e in [x for x in range(1,9) if x not in {i, j, k, m,q,w}]:
                            for r in [x for x in range(1,9) if x not in {i, j, k, m,q,w,e}]:
                                l = [i,j,k,m,q,w,e,r]
                                if check(l):
                                    ans.append(l)
for i in range(n):
    m = int(input())
    print(*ans[m-1],sep='')
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-11-03 000714.png)

### 189A. Cut Ribbon
brute force, dp 1300 https://codeforces.com/problemset/problem/189/A
思路：
代码：

```python
l = list(map(int, input().split()))
n = l[0]
abc = l[1:]
abc.sort()
m = n % abc[0]
p = n //abc[0]
ans = []
q = 0
def check(m,a,b):
    global p,q
    q = p
    k = 0
    if m %a ==0:
        p += m //a
        q = p-q
        return True
    while m >0:
        if m % b ==0:
            p += m//b
            p +=k
            q = p -q
            return True
        m -=a
        k +=1
    return False

if m ==0:
    print(n //abc[0])
else:
    while m <= n:
        if check(m,abc[1],abc[2]):
            ans.append(p)
            p -=q
            q =0
        m+=abc[0]
        p-=1
    print(max(ans))
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-11-03 234853.png)

## 2. 学习总结和收获
<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概 2024fall ”每日选做 、CF、LeetCode、洛谷
等网站题目。</mark>

因为期中考试的缘故，这周完全没有时间跟上每日选做了。明显感觉这周布置的题目难度突然可怕了许多。自己之前对dp，dfs算法都不太熟悉，这周的作业比起练习更多是学习解答中的思路。我感觉自己有很多思路还没法很好地用代码表示，不过现在更容易看懂别人的代码了。