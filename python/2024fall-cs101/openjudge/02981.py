n = str(int(input()))
m = str(int(input()))
N = len(n)
M = len(m)
NM = max(N,M)
up = False
up_0 = False
answers = []
if N >M:
    m = ['0']*(N-M) + list(m)
elif M >N:
    n = ['0']*(M-N) + list(n)

for i in range( max( N , M ) ):
    if i < max( N , M )-1:
        k = int(n[NM-i-1]) + int(m[NM-i-1])
        if up:
            k +=1
            up =False
        if k >=10:
            k -=10
            up = True
        answers.insert(0,k)
    else:
        k = int(n[NM-i-1]) + int(m[NM-i-1])
        if up:
            k +=1
            up =False
        if k >= 10:
            k -= 10
            up_0 = True
        answers.insert(0,k)
if up_0:
    answers.insert(0,1)
print(''.join(map(str,answers)))