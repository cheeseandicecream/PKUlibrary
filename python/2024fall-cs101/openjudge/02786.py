n = int(input())
for i in range(n):
    m = int(input())
    print(round(( 2**(-1.5) *( (1 + 2**0.5)**m - (1 - 2**0.5)**m ) )%32767 ))
