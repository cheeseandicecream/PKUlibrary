# Assignment #4: T-primes + 贪心
## 1. 题目
### 34B. Sale
greedy, sorting, 900, https://codeforces.com/problemset/problem/34/B
思路：

将所有电视的价格按大小排列，取最小的前m个讨论正负

代码

```python
n_m = list(map(int, input().split()))
n = n_m[0]
m = n_m[1]
prices = list(map(int, input().split()))
k = 0
prices.sort(reverse=True)
for i in range(m):
    if prices[n-i-1] <0:
        k -= prices[n-i-1]
print(k)
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-10-20 145113.png)

### 160A. Twins
greedy, sortings, 900, https://codeforces.com/problemset/problem/160/A
思路：

把硬币的面值按大小排列，依次相加，直到超过总额的一半。

代码

```python
n = int(input())
numbers = list(map(int, input().split() ))
numbers.sort(reverse=True)
m = 0
k = 0
for i in range(n):
    m += numbers[i]
    k += 1
    if m > sum(numbers)/2 :
        break
print(k)
```
代码运行截图 ==（至少包含有"Accepted"）==

![](D:\Pictures\Screenshots\屏幕截图 2024-10-20 145033.png)

### 1879B. Chips on the Board
constructive algorithms, greedy, 900,
https://codeforces.com/problemset/problem/1879/B
思路：

实际上，最节省的方案就是在最小的地方排一整列或一整行，只要比较这两种方案即可

代码

```python
t = int(input())
j=0
k=0
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    j = sum(a) + min(b)*n
    k = sum(b) + min(a)*n
    print(min(j,k))
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>
### 158B. Taxi
*special problem, greedy, implementation, 1100,
https://codeforces.com/problemset/problem/158/B
思路：

仿照装箱问题，先找出人数分别是1，2，3，4的小组个数，在讨论完2，3，4之后在剩下的空位塞入1人小组

代码

```python
import math
n = int(input())
groups = list(map(int, input().split()))
a = groups.count(1)
b = groups.count(2)
c = groups.count(3)
d = groups.count(4)
k = d + c + math.ceil(b/2)
a -= c + 2*(b - (b//2)*2 )
if a >0:
    k += math.ceil(a/4)
print(k)
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-10-20 153856.png)

### *230B. T-primes（选做）
binary search, implementation, math, number theory, 1300,
http://codeforces.com/problemset/problem/230/B
思路：

在查看题解后采用了欧拉筛方法

代码

```python
n = int(input())

def euler_sieve(m):
    is_prime = [True for i in range(m+1)]
    is_prime[1] = is_prime[0] = False
    prime = []
    for i in range(2, m+1):
        if is_prime[i]:
            prime.append(i)
        for p in prime:
            if i * p > m:
                break
            is_prime[i*p] = False
            if i % p == 0:
                break
    return is_prime

s = euler_sieve(10**6)

numbers =list(map(int,input().split()))
for number in numbers:
    if number**0.5 %1 != 0:
        print('NO')
    else:
        if s[int(number**0.5)]:
            print('YES')
        else:
            print('NO')
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](D:\Pictures\Screenshots\屏幕截图 2024-10-20 153935.png)

### *12559: 最大最小整数 （选做）
greedy, strings, sortings, http://cs101.openjudge.cn/practice/12559
思路：
代码
```python
```
代码运行截图 <mark>（至少包含有"Accepted"）</mark>
## 2. 学习总结和收获
感觉随着题目的不断增加，我也开始对不同题目的解法有一种共通的理解，现在经常发现很多题目的思路很熟悉，开始有些融会贯通。但对于全新思路的题目，我目前还经常想不到。

最近我的时间开始有些紧张，跟每日选做有些掉队。