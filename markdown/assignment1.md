## 02733：判断闰年

```
a = int(input())

if a % 4 == 0:
    if a % 100 == 0:
        if a % 400 == 0:
            if a % 3200 == 0:
                print("N")
            else:
                print("Y")
        else:
            print("N")
    else:
        print("Y")
else:
    print("N")
```

思路：用判断语句穷举

时间：24ms

![图片没显示](D:\Pictures\Screenshots\屏幕截图 2024-09-16 232804.png)



## 02750：鸡兔同笼

~~~
a = int(input())
if a % 2 != 0:
    print('0 0')
else:
    if a % 4 ==0:
        print(f'{a//4} {a//2}')
    else:
        print(f'{(a+2)//4} {a//2}')
~~~

时间：23ms

![图片未显示](D:\Pictures\Screenshots\屏幕截图 2024-09-16 234147.png)

## 50A.Domino piling

```
a = input().split()
M = int(a[0])
N = int(a[1])
if (M*N) % 2 == 0:
    print(int((M*N)/2))
else:
    print(int((M*N-1)/2))
```

思路：判断奇偶，用.split接受输入

时间：120ms

![图片未显示](D:\Pictures\Screenshots\屏幕截图 2024-09-16 235508.png)

## 1A.Theatre Square

```
i = input().split()
n = int(i[0])
m = int(i[1])
a = int(i[2])
if n % a ==0:
    x = int(n/a)
else:
    x = int(n//a + 1)
if m % a ==0:
    y = int(m/a)
else:
    y = int(m//a + 1)
print(x*y)
```

时间：60ms

![图片未显示](D:\Pictures\Screenshots\屏幕截图 2024-09-17 010825.png)

## 112A. Petya and Strings

```
a = input().lower()
b = input().lower()
if a > b:
    print(1)
elif a < b:
    print(-1)
else:
    print(0)
```

时间：120ms

![图片未显示](D:\Pictures\Screenshots\屏幕截图 2024-09-17 011447.png)

## 231A. Team

```
n = int(input())
number = 0
for i in range(n):
    a,b,c = [int(x) for x in input().split()]
    if a+b+c > 1:
        number += 1
print(number)
```

时间：120ms

![图片未显示](D:\Pictures\Screenshots\屏幕截图 2024-09-17 011645.png)

## 学习总结和收获

我是本人没学过python，当闫老师还没等我们选上课就开始布置作业的时候，我都惊呆了。这也推动我在军训期间一直在看推荐的那本蟒蛇书。等我看完半本书，发现自己还是做不对每日选做的题目。随着一直跟着练习每日选做，我明显感觉自己的编程水平有所提高，连带数学思维都更活跃了。真是纸上得来终觉浅。

我发现python的同一个功能能源完全不同的代码实现：

```
numbers = list(map(int,input().split()))
```

```
numbers = [int(x) for x in input().split()]
```

可谓法无定法啊。

我目前跟着做每日选做到了9.16号。
