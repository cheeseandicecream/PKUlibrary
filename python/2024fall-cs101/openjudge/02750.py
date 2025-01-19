a = int(input())
if a % 2 != 0:
    print('0 0')
else:
    if a % 4 ==0:
        print(f'{a//4} {a//2}')
    else:
        print(f'{(a+2)//4} {a//2}')