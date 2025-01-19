k= int(input())
for i in range(k):
    n = int(input())
    mis = [list(map(int,input().split())) for _ in range(n)]
    mis.sort()
    m = mis[-1][0]
    l = 1
    for j in range(n-2,-1,-1):
        if mis[j][1]<m:
            m = mis[j][0]
            l+=1
    print(l)