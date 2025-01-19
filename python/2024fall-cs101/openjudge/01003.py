a = 1
while a ==1 :
    n = float(input())
    if n == 0.00:
        break
    j = 2
    if n !=0:
        while n> 0:
            n -= 1/j
            j += 1
        print(f'{j-2} card(s)')