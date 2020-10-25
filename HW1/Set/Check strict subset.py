supset=set(input().split())
m=0
for i in range(int(input())):
    subset=set(input().split())
    if (supset.difference(subset)==set() or subset.difference(supset)!=set()):
        print("False")
        m=1
        break
if m==0: print('True')