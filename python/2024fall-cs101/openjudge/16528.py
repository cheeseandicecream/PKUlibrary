n = int(input())
acs = []
for i in range(n):
   ac = list(map(int, input().split()))
   acs.append(ac)
acs.sort()
m = 1
r = float('inf')
for i in range(n):
    if acs[i][0]<=r:
        if acs[i][1]<=r:
            r = acs[i][1]
    else:
        m+=1
        r = acs[i][1]
print(m)