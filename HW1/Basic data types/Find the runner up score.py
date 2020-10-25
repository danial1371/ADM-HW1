n = int(input())
s=input()
mylist=list(map(int, s.split()))
if len(mylist)!=n:
    raise ValueError
z = max(mylist)
while max(mylist) == z:
    mylist.remove(max(mylist))

print (max(mylist))
