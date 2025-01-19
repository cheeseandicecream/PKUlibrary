n = int(input())
a = list(map(int, input().split()))
a.sort()
b = [x for x in range(1,n+1)]
c = []
for i in a:
    if i in b:
        b.remove(i)
    elif i >n:
        c.append(i)
print(*b)
print(*c)
