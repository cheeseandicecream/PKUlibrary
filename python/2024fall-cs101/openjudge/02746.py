while True:
    n,m = map(int,input().split())
    k = 1
    if n == m == 0:
        break
    monkeys = [i for i in range(n+1)]
    while len(monkeys) >2:
        k += m - 1
        while k >n:
            k = k-n
        del monkeys[k]
        n-=1

    print(monkeys[1])
