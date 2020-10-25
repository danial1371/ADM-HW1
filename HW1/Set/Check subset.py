n=int(input())
for i in range(n):
    input()
    a=set(input().split())
    input()
    b=set(input().split())
    if a.difference(b)==set():
        print('True')
    else:
        print('False')