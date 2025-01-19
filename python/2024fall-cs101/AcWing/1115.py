def pick(a,b,i):
    if a %b ==0 :
        return i
    if a >=2*b :
        return i
    return pick(b,a-b,i+1)

while True:
    a,b = map(int,input().split())
    if a == b ==0:
        break
    if a < b:
        a,b = b,a
    if pick(a,b,0) % 2 ==0:
        print('win')
    else:
        print('lose')