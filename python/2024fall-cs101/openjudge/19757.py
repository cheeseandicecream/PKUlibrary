while True:
    r,n= map(int,input().split())
    if r==n==-1:
        break
    s=list(map(int,input().split()))
    s.sort()
    m =0
    i=0
    while i<n:
        start = s[i]
        i+=1
        while i<n and s[i]<=start+r:
            i+=1
        p = s[i-1]
        while i<n and s[i]<=p+r:
            i+=1
        m+=1
    print(m)