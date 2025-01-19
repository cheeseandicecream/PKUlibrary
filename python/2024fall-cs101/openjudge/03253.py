while True:
    n,p,m = map(int,input().split())
    if n ==p==m==0:
        break
    boys = [i for i in range(n+1)]
    out_boys = []
    while len(boys)>1:
        p +=m-1
        while p>n:
            p-=n
        out_boy = boys.pop(p)
        out_boys.append(out_boy)
        n-=1
    print(','.join(map(str,out_boys)))