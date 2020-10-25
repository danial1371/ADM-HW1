N=int(input())
myl=[]
for n in range(N):
    inp=list(input().split())
    if inp[0]=='insert': myl.insert(int(inp[1]),int(inp[2]))
    if inp[0]=='print' : print(myl)
    if inp[0]=='remove': myl.remove(int(inp[1]))
    if inp[0]=='append': myl.append(int(inp[1]))
    if inp[0]=='sort': myl.sort()
    if inp[0]=='pop': myl.pop(-1)
    if inp[0]=='reverse': myl.reverse()
