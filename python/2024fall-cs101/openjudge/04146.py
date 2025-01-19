n = int(input())

def check(m,p):
    for x  in range(0,int(2.5*m)+1):
        for y in range(0,int((5/3)*m)+1):
            if 0<=3*y +2*x -5*m<=p and 5*m - 3*y <=p and 5*m -2*x<=p:
                return True
    return False

for z in range(int( (3*n)//5 ),-1,-1):
    if check(z,n):
        print(5*z)
        break