n = int(input())
m = bin(n)[2:]
if m == m[::-1]:
    print('Yes')
else:
    print('No')