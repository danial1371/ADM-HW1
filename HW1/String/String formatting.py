def print_formatted(k):
    w = len(bin(k)[2:])
    for i in range(1,k+1):
        print(str(i).rjust(w,' '),oct(i)[2:].rjust(w,' '),hex(i)[2:].upper().rjust(w,' '),bin(i)[2:].rjust(w,' '))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
