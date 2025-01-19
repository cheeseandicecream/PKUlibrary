h = int(input())
m = int(input())
ans = 0
classes = []
l = 0
for i in range(m):
    s,c =map(float,input().split())
    classes.append([s*c,s,c])
classes.sort(reverse=True)
k = 2*h -0.5*m
for cl in classes:
    k -=5/cl[1]
    ans +=cl[0]*5/cl[1]
    if k <=0:
        ans +=k*cl[0]
        break
print(round(ans,1))