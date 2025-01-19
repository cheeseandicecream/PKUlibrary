sentence = input()
for i in sentence:
    if i.isupper():
        i =i.lower()
    else:
        i =i.upper()
    print(i,end='')
