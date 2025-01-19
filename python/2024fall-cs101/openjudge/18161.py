A,B,C = [],[],[]

a,b = map(int,input().split())
for i in range(a):
    A.append(list(map(int,input().split())))

c,d = map(int,input().split())
for i in range(c):
    B.append(list(map(int,input().split())))

e,f = map(int,input().split())
for i in range(e):
    C.append(list(map(int,input().split())))

D = [[0 for _ in range(f)] for _ in range(e)]
if b != c or a != e or d != f:
    print('Error!')
else:
    for i in range(e):
        for j in range(f):
            for k in range(b):
                D[i][j] += A[i][k]*B[k][j]
            D[i][j]  +=C[i][j]
    for i in D:
        print(*i)

