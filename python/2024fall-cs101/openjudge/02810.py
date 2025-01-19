n = int(input())
l = []
for a in range(1,n+1):
    for b in range(a,1,-1):
        for c in range(b,1,-1):
            for d in range(c,1,-1):
                if a**3 == b**3 + c**3 + d**3:
                    l.append((a,d,c,b))
l.sort()
for i in l:
    print(f'Cube = {i[0]}, Triple = ({i[1]},{i[2]},{i[3]})')