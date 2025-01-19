f = list(input())
n = len(f)
def one(x):
    if f[x-1] =='R':
        f[x-1] = 'B'
    elif f[x-1] =='B':
        f[x-1] = 'R'

def more(k,f):
    for x in range(k):
        if f[x] == 'R':
            f[x] = 'B'
        elif f[x] == 'B':
            f[x] = 'R'
    return f

dp1 = [[0,'']*(n+1)]
dp2 = [[0,'']*(n+1)]
for i in range(n):
    if f[i] == 'B':
        dp1[i+1][0] = dp1[i][0]+1
        dp1[i+1][1] = f'{f[i]}'
    else:
        dp1[i+1] = dp1[i]
