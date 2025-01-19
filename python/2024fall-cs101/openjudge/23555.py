n,m1,m2=map(int,input().split())
X = []
Y = []
for i in range(m1):
    X.append(list(map(int,input().split())))
for j in range(m2):
    Y.append(list(map(int,input().split())))

dp = [[0 for _ in range(n)] for _ in range(n)]
for x in X:
    for y in Y:
        if x[1]==y[0]:
            dp[x[0]][y[1]]+=x[2]*y[2]
for i in range(n):
    for j in range(n):
        if dp[i][j] !=0:
            print(f'{i} {j} {dp[i][j]}')
