n = int(input())
k = []
while n != 0:
    if n % 2 == 0:
        k.append(0)
        n = n//2
    else:
        k.append(1)
        n = (n-1)//2
if k ==list(reversed(k)):
    print('Yes')
else:
    print('No')