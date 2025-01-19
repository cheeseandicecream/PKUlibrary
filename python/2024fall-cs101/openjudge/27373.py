m = int(input())
n = int(input())
numbers = input().split()
l = []
for number in numbers:
    if len(number) <=m:
        k = m - len(number)
        l.append( (number+f'{number[0]}'*k ,number) )
l.sort(reverse=True)
dp = ['']*(m+1)
for j in range(len(l)):
    number = l[j][1]
    f = len(number)
    for i in range(m-f,-1,-1):
        ou = dp[i] + number
        if not dp[i+f] or int(ou) > int(dp[i+f]):
            dp[i+f] = ou

print(int(dp[m]))