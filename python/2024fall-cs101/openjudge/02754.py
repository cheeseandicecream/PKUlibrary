n = int(input())

def check(l):
    for i in range(8):
        for j in range(i+1,8):
            if abs(l[i] - l[j]) == abs(i-j):
                return False
    return True

ans = []

for i in range(1,9):
    for j in [x for x in range(1,9) if x !=i]:
        for k in [x for x in range(1,9) if x not in {i,j}]:
            for m in [x for x in range(1,9) if x not in {i,j,k}]:
                for q in [x for x in range(1,9) if x not in {i, j,k,m}]:
                    for w in [x for x in range(1,9) if x not in {i, j, k, m,q}]:
                        for e in [x for x in range(1,9) if x not in {i, j, k, m,q,w}]:
                            for r in [x for x in range(1,9) if x not in {i, j, k, m,q,w,e}]:
                                l = [i,j,k,m,q,w,e,r]
                                if check(l):
                                    ans.append(l)
for i in range(n):
    m = int(input())
    print(*ans[m-1],sep='')