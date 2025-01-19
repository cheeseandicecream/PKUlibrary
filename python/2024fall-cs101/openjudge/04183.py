def che(m):
    for i in range(3,int(m**0.5)+1,2):
        if m%i ==0:
            return False
    return True

s = int(input())
if s % 2 ==1:
    print(2*(s-2))
else:
    k = s//2
    while k %2 ==0:
        k-=1
    while  not che(k) or not che(s-k):
        k-=2
    print(k*(s-k))