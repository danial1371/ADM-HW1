import re
s=input()
k=input()
j=0
if re.search(k,s):
    while j+len(k)<len(s):
        m=re.search(k,s[j:])
        print("({0}, {1})".format(j+m.start(), j+m.end()-1))
        j+=(m.start()+1)
else:
    print("(-1, -1)")