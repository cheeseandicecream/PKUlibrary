def check(number):
    if number ==2 :
        return True
    if number % 2 == 0 or number ==1 :
        return False
    for i in range(3,int(number**0.5)+1,2):
        if number % i == 0:
            return False
    return True
n = int(input())
if n %2 != 0 or n < 6:
    print('Error!')
else:
    k = 3
    while k <=(n-k) :
        if check(k) and check(n-k):
            print(f'{n}={k}+{n-k}')
        k += 2
