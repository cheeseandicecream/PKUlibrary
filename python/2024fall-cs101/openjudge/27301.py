n,a,b = map(int,input().split())
plants = list(map(int,input().split()))
x,y = a,b
i=0
j=n-1
k =0

if n ==1:
    print(0)
elif n ==2:
    print(0)
else:
    def water(a,x,i,plants):
        global k
        if x<plants[i]:
            k +=1
            return a-plants[i]
        else:
            return x-plants[i]

    while i<j:
        x = water(a,x,i,plants)
        i+=1
        y = water(b,y,j,plants)
        j-=1
    if i>j:
        print(k)
    else:
        if plants[i]>max(x,y):
            print(k+1)
        else:
            print(k)