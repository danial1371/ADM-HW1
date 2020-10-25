from collections import deque
d = deque()
n = int(input())
for i in range(n):
    t = input().split()
    if len(t) == 2:
        eval("d." + t[0] + "(" + t[1] + ")")
    else:
        eval("d." + t[0] + "()")
