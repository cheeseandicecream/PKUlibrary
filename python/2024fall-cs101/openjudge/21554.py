n = int(input())
times = list(map(int, input().split()))
stu = [ [times[i],i+1] for i in range(n) ]
stu.sort()
k = []
for i in range(n):
    k.append(stu[i][1])
print(*k)
s = 0
for i in range(n):
    s += stu[i][0]*(n-i-1)
print(f'{s/n:.2f}')