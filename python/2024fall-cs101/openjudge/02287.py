while True:
    n = int(input())
    if n == 0:
        break
    T_horses = list(map(int, input().split()))
    K_horses = list(map(int, input().split()))
    T_horses.sort()
    K_horses.sort()
    ans = 0
    lT = 0 ; rT = n-1
    lK = 0 ; rK = n-1
    while lT<=rT:
        if T_horses[lT]>K_horses[lK]:
            ans += 1
            lT +=1 ; lK += 1
        elif T_horses[rT]>K_horses[rK]:
            ans += 1
            rT -=1 ; rK -= 1
        else:
            if T_horses[lT]<K_horses[rK]:
                ans -=1
            lT +=1 ; rK -= 1
    print(ans*200)