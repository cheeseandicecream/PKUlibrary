nCase = int(input())
for _ in range(nCase):
    n,m,b = map(int,input().split())
    sk = []
    for j in range(n):
        t,x = map(int,input().split())
        sk.append([t,-x])
    sk.sort()
    t_0 = 0
    m_0 = 0
    mm = 0
    for i in range(n):
        if sk[i][0]<= t_0:
            continue
        if mm != sk[i][0]:
            m_0 =0
            mm =sk[i][0]
        b+=sk[i][1]
        m_0 +=1
        if m_0 ==m:
            t_0 = sk[i][0]
            m_0 = 0
        if b<=0:
            print(sk[i][0])
            break

    if b>0:
        print('alive')