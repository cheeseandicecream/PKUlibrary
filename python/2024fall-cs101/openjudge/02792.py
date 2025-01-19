n = int(input())
for i in range(n):
    s = int(input())
    a = int(input())
    alist = list(map(int, input().split()))
    b = int(input())
    blist = list(map(int, input().split()))
    m =0
    for aa in alist:
        for bb in blist:
            if aa + bb == s:
                m+=1
    print(m)