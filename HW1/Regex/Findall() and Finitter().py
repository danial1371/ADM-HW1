import re
v= 'aeiou'
c= 'bcdfghjklmnpqrstvwxyz'
r='(?<=[' +c + '])([' +v+']{2,})['+c+ ']'
match = re.findall(r, input(), re.IGNORECASE)
if match:
    print(*match, sep='\n')
else:
    print('-1')