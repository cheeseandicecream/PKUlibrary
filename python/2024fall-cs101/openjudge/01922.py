import math

while True:
    N = int(input())
    K = []
    if N == 0:
        break
    for i in range(N):
        a,b = map(int,input().split('\t'))
        if b >=0:
            K.append(math.ceil( (4500/a) * 3.6 +b))
    print(min(K))
