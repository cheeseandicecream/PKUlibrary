import math

while True:
    a,b,c,d,e,f = map(int,input().split())
    if a == b==c==d==e==f==0:
        break
    m = d + e + f
    rest =[0,5,3,1]
    m += math.ceil(c/4)
    spacelef = 5*d + rest[c%4]
    if b > spacelef:
        m += math.ceil((b-spacelef)/9)
    spaceleff = 36*(m-f) - 25*e - 16*d -9*c -4*b
    if a > spaceleff:
        m+= math.ceil((a-spaceleff)/36)
    print(m)