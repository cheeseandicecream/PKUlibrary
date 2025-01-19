# Assignment #7: Nov Mock Exam 立冬
Updated 1646 GMT+8 Nov 7, 2024
2024 fall, Complied by <mark>同学的姓名、院系</mark>
**说明：**
1 ）月考： 未现场参加<mark>（请改为同学的通过数）</mark> “ ”。考试题目都在 题库（包括计概、数算题目） 里面，
按照数字题号能找到，可以重新提交。作业中提交自己最满意版本的代码和截图。
2）请把每个题目解题思路（可选），源码 Python, 或者 C++（已经在 Codeforces/Openjudge 上 AC），截
图（包含 Accepted ），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用
word）。AC 或者没有 AC，都请标上每个题目大致花费时间。
3）提交时候先提交 pdf 文件，再把 md 或者 doc “ ”文件上传到右侧 作业评论 。Canvas 需要有同学清晰头像、提
交文件有 pdf、"作业评论"区有上传的 md 或者 doc 附件。
4）如果不能在截止前提交作业，请写明原因。
## 1. 题目
### E07618: 病人排队
sorttings, http://cs101.openjudge.cn/practice/07618/
思路：用两个列表区分老人和年轻人，分别按要求排序
代码：

```python
n = int(input())
old = []
you = []
for i in range(n):
    m,y = input().split()
    y = int(y)
    if y <60:
        you.append(m)
    else:
        old.append([y,n-i,m])
old.sort(reverse=True)
for i in old:
    print(i[2])
for i in you:
    print(i)
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-11-07 193232.png)

### E23555: 节省存储的矩阵乘法
implementation, matrices, http://cs101.openjudge.cn/practice/23555/
思路：由于没法用列表的顺序直接找到对应的矩阵元，我采用枚举的方法来找可以相乘的矩阵元，并将结果储存到一个nxn的列表中（其实还是矩阵乘法的老结果）
代码：

```python
n,m1,m2=map(int,input().split())
X = []
Y = []
for i in range(m1):
    X.append(list(map(int,input().split())))
for j in range(m2):
    Y.append(list(map(int,input().split())))

dp = [[0 for _ in range(n)] for _ in range(n)]
for x in X:
    for y in Y:
        if x[1]==y[0]:
            dp[x[0]][y[1]]+=x[2]*y[2]
for i in range(n):
    for j in range(n):
        if dp[i][j] !=0:
            print(f'{i} {j} {dp[i][j]}')

```
代码运行截图 ==（至少包含有"Accepted"）==

![](D:\Pictures\Screenshots\屏幕截图 2024-11-07 200043.png)

### M18182: 打怪兽
implementation/sortings/data structures, http://cs101.openjudge.cn/practice/18182/
思路：
代码：

```python
nCase = int(input())
for _ in range(nCase):
    n,m,b = map(int,input().split())
    sk = []
    for j in range(n):
        t,x = map(int,input().split())
        sk.append([t,-x])
    sk.sort()
    t_0 = 0
    m_0 = 0
    mm = 0
    for i in range(n):
        if sk[i][0]<= t_0:
            continue
        if mm != sk[i][0]:
            m_0 =0
            mm =sk[i][0]
        b+=sk[i][1]
        m_0 +=1
        if m_0 ==m:
            t_0 = sk[i][0]
            m_0 = 0
        if b<=0:
            print(sk[i][0])
            break

    if b>0:
        print('alive')
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>
### M28780: 零钱兑换 3
dp, http://cs101.openjudge.cn/practice/28780/
思路：用动态规划，生成一个列表，其第i个元素表示第i块钱最少需要多少硬币。
代码：

```python
n,m = map(int,input().split())
coins = list(map(int,input().split()))
dp = [0]+[float('inf') for i in range(m)]
for coin in coins:
    for i in range(coin,m+1):
        dp[i]= min(dp[i],dp[i-coin]+1)
print(dp[m])
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-11-07 204653.png)

### T12757: 阿尔法星人翻译官
implementation, http://cs101.openjudge.cn/practice/12757
思路：这里采用了类似数值和单位的方式区分不同英文字符，因为单独出现的twenty one之类的字符既可能是21，也可能是21x1000的开头，所以应当用一个数据储存起来（这里用的m）。但唯独hundred、thousand、million不同，它们总会有至少一个单词作为系数，也总是和什么东西相乘，故用tim来表示它们。但对于million来说，它只用与之前的所有字符对应值相乘即可；对于thousan来说，它则是和上一个million之间的所有字符相乘，对hundred来说，它则是和上一个million或thousand之间的所有字符相乘。从上面论述可以看出，储存的数值如果遇到million或thousand就不会再有东西和它相乘了，可以之间加进结果，但反之，hundred却不行。故用ed专门表示thousand和million。
代码：

```python
dic = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6,
       'seven':7, 'eight':8, 'nine':9, 'ten':10, 'eleven':11, 'twelve':12,
       'thirteen':13, 'fourteen':14, 'fifteen':15, 'sixteen':16,
       'seventeen':17, 'eighteen':18, 'nineteen':19, 'twenty':20,
       'thirty':30, 'forty':40, 'fifty':50, 'sixty':60, 'seventy':70,
       'eighty':80, 'ninety':90, 'hundred':100, 'thousand':1000, 'million':1000000}
tim = ['hundred', 'thousand', 'million']
ed = ['thousand', 'million']

word = input().split()
n = False
if word[0]=='negative':
    n = True
    del word[0]
m = dic[word[0]]
ans = 0
for i in range(1,len(word)):

    if word[i] in tim:
        m = m*dic[word[i]]
    else:
        m +=dic[word[i]]
    if word[i] in ed:
        ans +=m
        m =0
ans+=m
if n:
    print(-ans)
else:
    print(ans)
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-11-08 004711.png)

### T16528: 充实的寒假生活
greedy/dp, cs10117 Final Exam, http://cs101.openjudge.cn/practice/16528/
思路：原题目的是找到最多有几个活动时间互不重叠，实际上和每日选做中的04100思路是一致的。
代码：

```python
n = int(input())
acs = []
for i in range(n):
   ac = list(map(int, input().split()))
   acs.append(ac)
acs.sort()
m = 1
r = float('inf')
for i in range(n):
    if acs[i][0]<=r:
        if acs[i][1]<=r:
            r = acs[i][1]
    else:
        m+=1
        r = acs[i][1]
print(m)
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-11-08 003901.png)

## 2. 学习总结和收获
<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概 2024fall ”每日选做 、CF、LeetCode、洛谷
等网站题目。</mark>

感觉这次的月考题比上周的作业题简单不少，可能是因为经过上周的训练，我对新的算法熟悉了不少。

这次月考我感觉第五道题特别耗时间，但其原因只是因为样例不够。反倒是第六题很快就做出来了。感觉自己还是比较擅长找到新题和旧题的共通之处而不是处理新题，路漫漫其修远兮。

这周还在期中考试，等下周开始我就开始好好地补每日选做。