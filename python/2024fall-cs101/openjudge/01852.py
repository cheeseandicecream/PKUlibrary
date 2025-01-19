t = int(input())
for i in range(t):
    l,n =map(int,input().split())
    ants = list(map(int,input().split()))
    maxtime = max(ants[0],int(l-ants[0]))
    mintime = min(ants[0],int(l-ants[0]))
    for ant in ants:
        anttime = [ant,l-ant]
        anttime.sort()
        if anttime[0] > mintime:
            mintime = anttime[0]
        if anttime[1] > maxtime:
            maxtime = anttime[1]
    print(f'{mintime} {maxtime}')