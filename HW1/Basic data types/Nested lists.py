if __name__ == '__main__':
    scorel=[]
    nestl=[]
    ans=[]
    n=int(input())
    for _ in range(n):
        name = input()
        score = float(input())
        nest=[name,score]
        scorel.append(score)
        nestl.append(nest)
x=min(scorel)
while x==min(scorel):
    scorel.remove(min(scorel))
x=min(scorel)
for i in range(n):
    if nestl[i][1]==x:
        ans.append(nestl[i][0])
ans=sorted(ans)
for i in range(len(ans)):
    print(ans[i])


