t = int(input())

for i in range(t):
    n = int(input())
    k =0
    m =[]
    while 2**k<n:
        m.append(2**k)
        k+=1
    print( n*(n+1)//2 -2*sum(m) )
