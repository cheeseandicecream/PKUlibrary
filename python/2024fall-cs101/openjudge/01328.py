import math
m = 1
while True:
    n,d = map(int,input().split())
    if n ==0 and d == 0:
        break

    st = False
    islands = []
    ans = 1

    for i in range(n):
        x,y = map(int,input().split())
        if y > d:
            st = True
        else:
            delta = round(math.sqrt(d**2-y**2),2)
            islands.append([x-delta,x+delta])
    islands.sort()

    if st :
        print(f'Case {m}: -1')
        m+=1
        c = input()
        continue

    dp = float('inf')
    for i in range(n):
        if islands[i][0] <= dp:
            dp = min(dp, islands[i][1])
            continue
        ans+=1
        dp = islands[i][1]
    print(f'Case {m}: {ans}')
    m+=1
    c = input()