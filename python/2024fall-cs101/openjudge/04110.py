n,w = map(int,input().split())
values = []
for i in range(n):
    v,k = map(int,input().split())
    for j in range(k):
        values.append(v/k)
values.sort(reverse=True)
sell = sum(values[:w])
print(round(sell,1))