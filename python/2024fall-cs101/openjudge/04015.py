while True:
    try:
        n = input().strip()
        m = n.split('@')
        if n[0] =='@' or n[-1] =='@' or n[0] =='.' or n[-1] =='.':
            print('NO')
        elif len(m) == 2 and m[1][0] != '.' and '.' in m[1] and m[0][-1] != '.':
            print('YES')
        else:
            print('NO')
    except EOFError:
        break
