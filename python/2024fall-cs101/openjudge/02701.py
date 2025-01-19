n = int(input())
g = []

def ju(n):
    for i in str(n):
        if i =='7':
            return False
    return True

for i in range(1,n+1):
    if i % 7 != 0 and ju(i):
        g.append(i**2)

print(sum(g))
