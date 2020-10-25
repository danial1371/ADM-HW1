t= 'M{0,3}'
h= '(C[MD]|D?C{0,3})'
te= '(X[CL]|L?X{0,3})'
d= '(I[VX]|V?I{0,3})'
regex_pattern = t+h+te+d+'$'
import re
print(str(bool(re.match(regex_pattern, input()))))