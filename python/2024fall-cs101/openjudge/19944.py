n = int(input())
for i in range(n):
    time = str(input())
    year = int(time[0:4])
    month = int(time[4:6])
    day = int(time[6:8])

    if month ==1 or month ==2:
        month +=12
        year -=1
    c = int(str(year)[0:2])
    y = int(str(year)[2:4])
    w = int( (y + int(y/4) + int(c/4) - 2*c + 26*(month+1)/10 +day -1) % 7 )
    if w==0:
        print('Sunday')
    if w==1:
        print('Monday')
    if w==2:
        print('Tuesday')
    if w==3:
        print('Wednesday')
    if w==4:
        print('Thursday')
    if w==5:
        print('Friday')
    if w==6:
        print('Saturday')
