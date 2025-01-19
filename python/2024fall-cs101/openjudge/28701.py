n,k = map(int,input().split())
chickens = list(map(int,input().split()))
s = sum(chickens)
chickens.sort(reverse=True)
for i in range(n):
    if chickens[i] <=s/k:
        break
    k -=1
    s -= chickens[i]
ans = f'{s/k:.3f}'
print(ans)