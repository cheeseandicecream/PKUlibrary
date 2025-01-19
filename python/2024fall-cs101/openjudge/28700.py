a = input()

int_to_str = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC')
              ,(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]

str_to_int = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

number = 0
message = []

if 'A'<=a[0]<='Z':
    v = 0
    pre_v = 0
    for l in a:
        v = str_to_int[l]
        if v >pre_v:
            number+=v -2*pre_v
        else:
            number+=v
        pre_v=v
    print(number)
else:
    a = int(a)
    for i in range(13):
        if a >= int_to_str[i][0]:
            message.append(int_to_str[i][1]*(a//int_to_str[i][0]))
            a = a % int_to_str[i][0]
    print(''.join(message))