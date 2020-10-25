def merge_the_tools(s, k):
    t=[]
    n=int(len(s)/k)
    for i in range(n):
        t.append(s[k*i:(i+1)*k])
    w=[]
    for x in t:
        l=''
        for j in x:
            if j not in l:
                l+=j
        w.append(l)
    for t in w:
        print(t)