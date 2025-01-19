H_month = { 'pop':0,'no':20,'zip':40,'zotz':60,'tzec':80,'xul':100,
            'yoxkin':120,'mol':140,
            'chen':160,'yax':180,'zac':200,'ceh':220,'mac':240,
            'kankin':260,'muan':280,'pax':300,'koyab':320,'cumhu':340,'uayet':360}

T_name = {1:'imix',2:'ik',3:'akbal',4:'kan',5:'chicchan',6:'cimi',
          7:'manik',8:'lamat',9:'muluk',10:'ok',11:'chuen',12:'eb',
          13:'ben',14:'ix',15:'mem',16:'cib',17:'caban',18:'eznab',
          19:'canac',20:'ahau'}

n = int(input())
print(n)
for i in range(n):
    T_da = []
    da = list(map(str, input().split()))
    day = int(float(da[0]))
    s_d = day + 365*int(da[2]) + H_month[da[1]]
    T_da.append(s_d //260)
    s_d -= T_da[0]*260
    T_da.insert(0,s_d%13 +1)
    T_da.insert(1,T_name[s_d%20 +1])
    print(*T_da)