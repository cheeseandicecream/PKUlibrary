p = int(input())
w = list(map(int, input().split()))
w.sort()
a = 0
b = 0
while len(w)>0:
    while p >0 and len(w)>0:
        if p >= w[0]:
            p -= w.pop(0)
            a += 1
        else:
            break
    if len(w) ==1 or len(w) == 0:
        break
    if a >b:
        p += w.pop(-1)
        b+=1
    else:
        break
print(a-b)