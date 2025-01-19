s = input()
s = s.lower()

date = 'hello'
num = 0

for i in s:
    if i == date[num] :
        num +=1
    if num ==5:
        break
if num ==5:
    print('YES')
else:
    print('NO')
