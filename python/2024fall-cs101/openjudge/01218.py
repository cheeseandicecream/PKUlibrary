m = int(input())
for i in range(m):
    n = int(input())
    ceil = [1 for _ in range(n)]
    for j in range(2,n+1):
        b = j-1
        while b < n:
            if ceil[b] == 1:
                ceil[b] = 0
            else:
                ceil[b] = 1
            b +=j
    print(sum(ceil))