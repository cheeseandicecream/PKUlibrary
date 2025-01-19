import math
while True:
    a,b,c,d,e,f = map(int,input().split())
    if a==b==c==d==e==f==0:
        break
    m = d + e + f + math.ceil(c/4)
    restb = [0,5,3,1]
    resta = [0,11,6,5]
    b -= (5*d + restb[c%4])
    if b>0:
        m += math.ceil(b/9)
        a -= resta[c%4] + 11*e
    else:
        a -= (-4*b + resta[c%4] + 11*e)

    if a>0 and b %9==0:
        m += math.ceil(a/36)
    elif a>0 and b%9!=0 and b>0:
        a -= (36 - 4*(b%9))
        if a>0:
            m += math.ceil(a/36)
    print(m)