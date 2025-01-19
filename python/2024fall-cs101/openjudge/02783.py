while True:
    N = int(input())
    if N == 0:
        break
    hotel =[]
    m=1
    for i in range(N):
        distance,cost =map(int,input().split())
        hotel.append([distance,cost])
    hotel.sort()
    min_cost = hotel[0][1]
    for i in range(N):
        if hotel[i][1] < min_cost:
            m+=1
            min_cost = hotel[i][1]
    print(m)