n = int(input())
ans = []
l = []
def queen(ans,l):
    if len(l)==8:
        ans.append(l.copy())
        return
    for i in [x for x in range(1,9) if x not in l]:
        q = 0
        for j in range(len(l)):
            if abs(i - l[j]) == abs(len(l)-j):
                q = 1
                break
        if q == 1:
            continue
        l.append(i)
        queen(ans,l)
        l.pop()

queen(ans,l)
for i in range(n):
    m = int(input())
    print(*ans[m-1],sep='')
