if __name__ == '__main__':
    s = input()
    k=0
    for a in s:
        if a.isalnum():
            print("True")
            break
        else: k+=1
    if k==len(s): print("False")
    k=0
    for a in s:
        if a.isalpha():
            print("True")
            break
        else: k+=1
    if k==len(s): print("False")
    k=0
    for a in s:
        if a.isdigit():
            print("True")
            break
        else: k+=1
    if k==len(s): print("False")
    k=0
    for a in s:
        if a.islower():
            print("True")
            break
        else: k+=1
    if k==len(s): print("False")
    k=0
    for a in s:
        if a.isupper():
            print("True")
            break
        else: k+=1
    if k==len(s): print("False")
    k=0

