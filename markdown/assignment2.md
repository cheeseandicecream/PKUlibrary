## 1.题目

### 263A. Beautiful Matrix

思路：

数学思维，计算中心元素和待处理元素x坐标和y坐标之差。

##### 代码

```
x_i = 0
y_j = 0
 
for i in range(5):
    line = [int(x) for x in input().split()]
    for j in range(5):
        if line[j] != 0:
            x_i = i
            y_j = j
            break
print( abs(x_i-2) + abs(y_j-2) )
```

代码运行截图：

![图片未显示](D:\Pictures\Screenshots\屏幕截图 2024-09-27 155312.png)

用时：120ms



### 1328A. Divisibility Problem

思路：

数学思维，先计算两个数之间的余数，由此可以直接得到步数

##### 代码

~~~
n = int(input())
answers = n * [0]
for i in range(n):
    a, b = map(int, input().split())
    if a % b == 0:
        answers[i] = 0
    else:
        answers[i] = (b - (a%b))
for answer in answers:
    print(answer)
~~~

代码运行截图：

![图片未显示](D:\Pictures\Screenshots\屏幕截图 2024-09-27 160129.png)

用时：50ms



### 427A.Police Recruits

思路：

计算机思维，逐次加上个数字，如果犯罪案件导致计数为负，另外计数。

##### 代码

```
t = int(input())
m = 0
n = 0
k = map(int, input().split())
for i in k:
    m +=i
    if m<0 and i<0:
        n -= i
        m -=i
print(n)
```

代码运行截图：

![图片未显示](D:\Pictures\Screenshots\屏幕截图 2024-09-27 160906.png)

用时：45ms



### 02808：校门外的树

思路：

计算机思维，构造和路上的树类似的集合

##### 代码

```
l , m = map(int, input().split())
region = (l+1)*[1]
for i in range(m):
    x,y = map(int, input().split())
    for j in range(x-1, y):
        region[j] = 0
print(sum(region))
```

代码运行截图：

![图片未显示](D:\Pictures\Screenshots\屏幕截图 2024-09-27 161426.png)

用时：46ms



### sy60：水仙花数Ⅱ

思路：

计算机思维，将数字转化为字符串来使用每一位的数字，一个个判断是否是水仙花数。

##### 代码

```
def check(m):
    if m == sum(int(x)**3 for x in str(m)):
        return True
    return False

a,b = map(int,input().split())
num = []
while a<=b:
    if check(a):
        num.append(a)
    a+=1
if len(num) !=0:
    print(*num)
else:
    print('NO')
```

代码运行截图：

![](D:\Pictures\Screenshots\屏幕截图 2024-09-27 162511.png)用时：0ms（晴问显示的。。。)



### 01922:Ride to school

思路：考虑到骑手的速度恒定，这意味着Charley最后会跟着最先到达的骑手（只要骑手出发时间非负）

##### 代码

```
import math

while True:
    N = int(input())
    K = []
    if N == 0:
        break
    for i in range(N):
        a,b = map(int,input().split('\t'))
        if b >=0:
            K.append(math.ceil( (4500/a) * 3.6 +b))
    print(min(K))
```

代码运行截图：

![图片未显示](D:\Pictures\Screenshots\屏幕截图 2024-10-04 172042.png)

用时：48ms



## 2.学习总结和收获

随着代码难度提高，我感觉题目对数学思维的要求越来越高，同时计算机思维的解题思路变得越来越繁琐。在练习许多题目后，我感觉自己思考问题都比以前严谨了许多。

题目难度上升，开始出现许多全新的代码，我开始用AI辅助学习，当我想实现某个我不知道对应代码的功能时，我会问AI对应的代码；当我在题目解答中遇到没见过的代码时，我也会让AI给我讲解相应的知识点。我发现把解题和AI结合起来的学习方式非常高效，可谓是“AI训练人类大模型”。

