import re
b=re.search(r'([a-zA-Z0-9])\1+', input())
if b:
    print(b.group(1))
else:
    print(-1)