n = int(input())
a,b = map(int,input().split())
l = a
lr = []
for i in range(n):
    x,y = map(int,input().split())
    lr.append(x*y)
    l = l*x
lr.sort(reverse=True)
print(l//lr[0])