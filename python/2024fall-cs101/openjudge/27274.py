import math
from math import floor

s = input()
k = floor(math.log(len(s),2))
code = []
for i in range(k+1):
    code.append(s[2**i-1])
ans = ''
for i in range(len(code)//2):
    ans = ans + code[i]
    ans = ans + code[-i-1]
if len(code) % 2 == 1:
    ans = ans + code[len(code)//2]
print(ans)