n = int(input())
for _ in range(n):
    p = int(input())
    if p%19 == 0:
        print('Yes')
    else:
        pp = str(p)
        relate = False
        for i in range(len(pp)-1):
            if pp[i:i+2] == '19':
                relate = True
                break
        if not relate:
            print('No')
        else:
            print('Yes')