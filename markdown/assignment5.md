# Assignment #5: Greedy 穷举 Implementation
Updated 1939 GMT+8 Oct 21, 2024
2024 fall, Complied by <mark>王思杰、物理学院</mark>
**说明：**
1）请把每个题目解题思路（可选），源码 Python, 或者 C++（已经在 Codeforces/Openjudge 上 AC），截
图（包含 Accepted ），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用
word）。AC 或者没有 AC，都请标上每个题目大致花费时间。
3）提交时候先提交 pdf 文件，再把 md 或者 doc “ ”文件上传到右侧 作业评论 。Canvas 需要有同学清晰头像、提
交文件有 pdf、"作业评论"区有上传的 md 或者 doc 附件。
4）如果不能在截止前提交作业，请写明原因。

## 1. 题目
### 04148: 生理周期
brute force, http://cs101.openjudge.cn/practice/04148
思路：枚举其中一个生理周期的高峰，检查其他两个生理周期是否也处于高峰。
代码：

```python
m=0
while True:
    p,e,i,d = map(int,input().split())
    m += 1
    if p == e == i == d == -1:
        break
    while p-e<=0 or p -i<=0:
        p+=23
    while (p-e)%28 != 0 or (p-i)%33 != 0:
        p +=23
    print(f'Case {m}: the next triple peak occurs in {p-d} days.')
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-10-27 001648.png)

用时：24ms

### 18211: 军备竞赛

greedy, two pointers, http://cs101.openjudge.cn/practice/18211
思路：鸣人应当优先制造便宜的武器，出售昂贵的武器。对所有武器按大小排列后，每当鸣人每出售一把武器，至少能制造一把武器，除非已经没有武器可以制造了。故鸣人每卖出一把武器，都会竭尽所能地制造最多武器。

代码：

```python
p = int(input())
w = list(map(int, input().split()))
w.sort()
a = 0
b = 0
while len(w)>0:
    while p >0 and len(w)>0:
        if p >= w[0]:
            p -= w.pop(0)
            a += 1
        else:
            break
    if len(w) ==1 or len(w) == 0:
        break
    if a >b:
        p += w.pop(-1)
        b+=1
    else:
        break
print(a-b)
```
代码运行截图 ==（至少包含有"Accepted"）==

![](D:\Pictures\Screenshots\屏幕截图 2024-10-27 002143.png)

用时：26ms

### 21554: 排队做实验

greedy, http://cs101.openjudge.cn/practice/21554
思路：让用时少的人优先做实验即可。
代码：

```python
p = int(input())
w = list(map(int, input().split()))
w.sort()
a = 0
b = 0
while len(w)>0:
    while p >0 and len(w)>0:
        if p >= w[0]:
            p -= w.pop(0)
            a += 1
        else:
            break
    if len(w) ==1 or len(w) == 0:
        break
    if a >b:
        p += w.pop(-1)
        b+=1
    else:
        break
print(a-b)
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-10-27 011951.png)

用时：26ms

### 01008: Maya Calendar

implementation, http://cs101.openjudge.cn/practice/01008/
思路：类似上次月考的罗马数字，建立数字和字符串相互转化的字典
代码：

```python
H_month = { 'pop':0,'no':20,'zip':40,'zotz':60,'tzec':80,'xul':100,
            'yoxkin':120,'mol':140,
            'chen':160,'yax':180,'zac':200,'ceh':220,'mac':240,
            'kankin':260,'muan':280,'pax':300,'koyab':320,'cumhu':340,'uayet':360}

T_name = {1:'imix',2:'ik',3:'akbal',4:'kan',5:'chicchan',6:'cimi',
          7:'manik',8:'lamat',9:'muluk',10:'ok',11:'chuen',12:'eb',
          13:'ben',14:'ix',15:'mem',16:'cib',17:'caban',18:'eznab',
          19:'canac',20:'ahau'}

n = int(input())
print(n)
for i in range(n):
    T_da = []
    da = list(map(str, input().split()))
    day = int(float(da[0]))
    s_d = day + 365*int(da[2]) + H_month[da[1]]
    T_da.append(s_d //260)
    s_d -= T_da[0]*260
    T_da.insert(0,s_d%13 +1)
    T_da.insert(1,T_name[s_d%20 +1])
    print(*T_da)
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-10-27 114549.png)

用时：30ms

### 545C. Woodcutters

dp, greedy, 1500, https://codeforces.com/problemset/problem/545/C
思路：在决策过程中，只要有树往前一个树的方向倒或是不倒，剩下的树就完全不会受前面的树的影响，换句话说，如果有树往后一个树倒下，他也只会影响到一棵树。因此，每棵树在决策时只用考虑前一颗树。
代码：

```python
n = int(input())
trees = []
for i in range(n):
    x,h = map(int,input().split())
    trees.append([x,h])
trees.sort()
if len(trees) >= 2:
    m = 2
else:
    m =1
for i in range(1,n-1):
    if trees[i][1]<trees[i][0]-trees[i-1][0]:
        m+=1
    elif trees[i][1]<trees[i+1][0]-trees[i][0]:
        m+=1
        trees[i][0]+=trees[i][1]
print(m)
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-10-28 194002.png)

### 01328: Radar Installation
greedy, http://cs101.openjudge.cn/practice/01328/
思路：将（x，y）的二维坐标转化为在岸边可以放置雷达的区间，这样就把问题转换为如何用最少的雷达同时处于这些区间的问题。
代码：

```python
import math
m = 1
while True:
    n,d = map(int,input().split())
    if n ==0 and d == 0:
        break

    st = False
    islands = []
    ans = 1

    for i in range(n):
        x,y = map(int,input().split())
        if y > d:
            st = True
        else:
            delta = round(math.sqrt(d**2-y**2),2)
            islands.append([x-delta,x+delta])
    islands.sort()

    if st :
        print(f'Case {m}: -1')
        m+=1
        c = input()
        continue

    dp = float('inf')
    for i in range(n):
        if islands[i][0] <= dp:
            dp = min(dp, islands[i][1])
            continue
        ans+=1
        dp = islands[i][1]
    print(f'Case {m}: {ans}')
    m+=1
    c = input()
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-10-29 010535.png)

## 2. 学习总结和收获
<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概 2024fall ”每日选做 、CF、LeetCode、洛谷
等网站题目。</mark>

临近期中，明显感觉时间紧张了许多，每日选做也常常很难跟上，但开心的是水平也随老师布置题目的难度水涨船高。

现在我开始发现一些题目的通性，能从新题窥见老题的影子，得到相关的思路。比如这次作业的第六题：我没有想到怎么用几何的思路去解决，但发现倘若把（x，y）转换为岸边所对应可以放置雷达的范围，就把这道题转换为了之前做过的每日选做题。
