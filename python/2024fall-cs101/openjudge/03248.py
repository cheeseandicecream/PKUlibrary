while True:
    try:
        ab = list(map(int,input().split()))
        n = min(ab)
        while ab[0] % n !=0 or ab[1] % n != 0:
            n-=1
        print(n)
    except EOFError:
        break