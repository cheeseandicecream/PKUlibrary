import sys
data = sys.stdin.read().splitlines()
for i in range(0,len(data),2):
    n = int(data[i])
    l = list(map(int,data[i+1].split()))
    l.sort(reverse=True)
    s = sum(l)
    if l[0] >s//2:
        ans = s-l[0]
        print(f'{ans:.1f}')
    else:
        print(f'{s/2:.1f}')