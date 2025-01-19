dic = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6,
       'seven':7, 'eight':8, 'nine':9, 'ten':10, 'eleven':11, 'twelve':12,
       'thirteen':13, 'fourteen':14, 'fifteen':15, 'sixteen':16,
       'seventeen':17, 'eighteen':18, 'nineteen':19, 'twenty':20,
       'thirty':30, 'forty':40, 'fifty':50, 'sixty':60, 'seventy':70,
       'eighty':80, 'ninety':90, 'hundred':100, 'thousand':1000, 'million':1000000}
tim = ['hundred', 'thousand', 'million']
ed = ['thousand', 'million']

word = input().split()
n = False
if word[0]=='negative':
    n = True
    del word[0]
m = dic[word[0]]
ans = 0
for i in range(1,len(word)):

    if dic[word[i]]>m+ans and word[i] in tim:
        m = m*dic[word[i]]
        ans = ans*dic[word[i]]
    elif word[i] in tim:
        m = m*dic[word[i]]
    else:
        m +=dic[word[i]]
    if word[i] in ed:
        ans +=m
        m =0
ans+=m
if n:
    print(-ans)
else:
    print(ans)