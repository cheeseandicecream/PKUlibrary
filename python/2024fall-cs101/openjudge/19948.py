n,m = map(int,input().split())
stu = list(map(int,input().split()))
stu.sort()
minus = []
for i in range(n-1):
    minus.append(stu[i+1]-stu[i])
minus.sort(reverse=True)
print(stu[-1]-stu[0]-sum(minus[:m-1]))