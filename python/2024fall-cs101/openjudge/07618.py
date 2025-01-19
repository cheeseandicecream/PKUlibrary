n = int(input())
old = []
you = []
for i in range(n):
    m,y = input().split()
    y = int(y)
    if y <60:
        you.append(m)
    else:
        old.append([y,n-i,m])
old.sort(reverse=True)
for i in old:
    print(i[2])
for i in you:
    print(i)