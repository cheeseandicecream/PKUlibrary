## 1. 题目
### E28674:《黑神话：悟空》之加密
http://cs101.openjudge.cn/practice/28674/
思路：先判断字母大小写，在偏移定值后，保证偏移后还在字母表内。
代码

```python
k = int(input())
s = input()
ss = []
m=0
while k >26:
    k-=26
for i in range(len(s)):
    m = ord(s[i]) - k
    if ord(s[i])>90:
        while m <97 :
            m+=26
    else:
        while m < 65:
            m+=26
    ss.append(chr(m))
print(''.join(ss))
```
代码运行截图 ==（至少包含有"Accepted"）==

![](D:\Pictures\Screenshots\屏幕截图 2024-10-13 223843.png)

### E28691: 字符串中的整数求和
http://cs101.openjudge.cn/practice/28691/

思路：提取文本输入数据的前两位，再转化为整数。

代码

```python
a,b = input().split()
n = int(a[:2])
m = int(b[:2])
print(m+n)
```
代码运行截图 ==（至少包含有"Accepted"）==

![](D:\Pictures\Screenshots\屏幕截图 2024-10-13 223814.png)

### M28664: 验证身份证号
http://cs101.openjudge.cn/practice/28664/
思路：通过创建一个列表
代码

```python
n = int(input())
quanzhong = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
last = ['1','0','X','9','8','7','6','5','4','3','2']
for i in range(n):
    number = input()
    s = 0
    for j in range(17):
        s += quanzhong[j]*int(number[j])
    s = s%11
    if str(number[17]) == last[s]:
        print('YES')
    else:
        print('NO')
```
代码运行截图 ==（AC 代码截图，至少包含有"Accepted"）==

![](D:\Pictures\Screenshots\屏幕截图 2024-10-13 223723.png)

### M28678: 角谷猜想
http://cs101.openjudge.cn/practice/28678/
思路：按照题意，每步操作的同时输出字符串和数学式
代码

```python
n = int(input())
m =n
while m !=1:
    if m%2 ==0:
        m = m//2
        print(f'{2*m}/2={m}')
    else:
        print(f'{m}*3+1={3*m+1}')
        m =3*m+1
print('End')
```
代码运行截图 ==（AC 代码截图，至少包含有"Accepted"）==

![](D:\Pictures\Screenshots\屏幕截图 2024-10-13 224710.png)

### M28700: 罗马数字与整数的转换
http://cs101.openjudge.cn/practice/28700/
思路：用字典来检索每个字符对应的数值，用列表的顺序性依次减去每个数值并输出对应字符

##### 代码
```python
a = input()

int_to_str = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC')
              ,(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]

str_to_int = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

number = 0
message = []

if 'A'<=a[0]<='Z':
    v = 0
    pre_v = 0
    for l in a:
        v = str_to_int[l]
        if v >pre_v:
            number+=v -2*pre_v
        else:
            number+=v
        pre_v=v
    print(number)
else:
    a = int(a)
    for i in range(13):
        if a >= int_to_str[i][0]:
            message.append(int_to_str[i][1]*(a//int_to_str[i][0]))
            a = a % int_to_str[i][0]
    print(''.join(message))
```
代码运行截图 ==（AC 代码截图，至少包含有"Accepted"）==

![](D:\Pictures\Screenshots\屏幕截图 2024-10-14 000704.png)

### *T25353: 排队 （选做）
http://cs101.openjudge.cn/practice/25353/
思路：
代码

```python
```
代码运行截图 ==（AC 代码截图，至少包含有"Accepted"）==
## 2. 学习总结和收获

我发现平时注意学习答案可以学会很多精练且高效的代码方式，而这些很多是我自己难以想到的。在这次月考中，我发现很多思路其实并不来源于自己的灵光一闪，而是平时做题积累的经验带来的。

我发现开始能够要求自己去写出尽量简洁的代码实现目标，太好啦。
