def swap_case(mystr):
    newstr=''
    for a in mystr:
        if a.isupper()==True: newstr+=a.lower()
        elif a.islower()==True: newstr+=a.upper()
        else: newstr+=a
    return newstr
