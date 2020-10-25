n=int(input())
s1=set(input().split())
for i in range(int(input())):
    fu=input().split()
    if(fu[0] == "intersection_update"):
        s1.intersection_update(set(input().split()))
    elif(fu[0] == "update"):
        s1.update(set(input().split()))
    elif(fu[0] == "symmetric_difference_update"):
        s1.symmetric_difference_update(set(input().split()))
    elif(fu[0] == "difference_update"):
        s1.difference_update(set(input().split()))
print(sum(map(int,s1)))