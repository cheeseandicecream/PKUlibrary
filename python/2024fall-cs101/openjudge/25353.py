N, D = map(int, input().split())
h = [int(input()) for _ in range(N)]
pp = [False] * N

while False in pp:
    tempor = []
    for i in range(N):
        if pp[i]:
            continue
        if len(tempor) != 0:
            maxh = max(h[i], maxh)
            minh = min(h[i], minh)
        else:
            maxh = h[i]
            minh = h[i]
        if maxh - minh > 2*D:
            break
        if h[i]+D>=maxh and h[i]-D<=minh:
            tempor.append(h[i])
            pp[i] = True
    tempor.sort()
    for j in tempor:
        print(j)

