n = int(input())
a = []
while n % 2 ==0:
    n = int(n/2)
    a.append(2)

for i in range(3,int(n**0.5)+1,2):
    while n % i ==0:
        n = int(n/i)
        a.append(i)
if n > 1 :
    a.append(n)
if len(a) == len(set(a)) and len(a) %2 ==0:
    print(1)
elif len(a) == len(set(a)) and len(a) %2 ==1:
    print(-1)
else:
    print(0)
