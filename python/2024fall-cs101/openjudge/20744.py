items = list(map(int, input().split(',')))
n = len(items)
dp1 = [0]*n
dp2 = [0]*n
dp1[0] = items[0]
dp2[0] = items[0]
for i in range(1,n):
    dp1[i] = max(dp1[i-1]+items[i], items[i])
    dp2[i] = max(dp1[i-1], items[i],dp2[i-1]+items[i])
print(max(dp2))