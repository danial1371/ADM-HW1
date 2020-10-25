def count_substring(string, sub_string):
    l=len(sub_string)
    k=0
    for i in range(len(string)):
        if string[i]==sub_string[0]:
             if string[i:i+l]==sub_string: k+=1
    return k

