t = int(input())
for i in range(t):
    j = 0
    k = 0
    n = int(input())
    while n % 2 ==0:
        n = n//2
        j +=1
    while n % 3 == 0:
        n = n//3
        k +=1
    if n !=1:
        print(-1)
    elif j <= k:
        print(2*k-j)
    else:
        print(-1)