m=0
while True:
    p,e,i,d = map(int,input().split())
    m += 1
    if p == e == i == d == -1:
        break
    while p-e<=0 or p -i<=0:
        p+=23
    while (p-e)%28 != 0 or (p-i)%33 != 0:
        p +=23
    print(f'Case {m}: the next triple peak occurs in {p-d} days.')