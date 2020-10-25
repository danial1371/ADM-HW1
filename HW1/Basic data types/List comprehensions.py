if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
xx=[i for i in range(x+1)]
yy=[i for i in range(y+1)]
zz=[i for i in range(z+1)]
print([[i,j,k] for i in xx for j in yy for k in zz if i+j+k!=n ])
