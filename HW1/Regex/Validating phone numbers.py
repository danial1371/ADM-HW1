n=int(input())
for i in range(n):
    pn=input()
    if (len(pn)==10) and (pn.isnumeric()) :
        if pn[0] in ['7','8','9']:
            print('YES')
        else:
            print('NO')
    else: print('NO')