m,n,p,q = map(int,input().split())
matrix_1 = []
matrix_2 = []
ans = []
for i in range(m):
    matrix_1.append(list(map(int,input().split())))
for i in range(p):
    matrix_2.append(list(map(int,input().split())))
for k in range(m+1-p):
    el = []
    for j in range(n+1-q):
        s = 0
        for x in range(p):
            for y in range(q):
                s+=matrix_2[x][y]*matrix_1[x+k][y+j]
        el.append(s)
    ans.append(el)
for i in ans:
    print(*i)