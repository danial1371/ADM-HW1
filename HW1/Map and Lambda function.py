cube = lambda x: x ** 3


def fibonacci(n):
    if n == 0:
        r = []
    if n == 1:
        r = [0]
    if n == 2:
        r = [0, 1]
    if n > 2:
        r = [0, 1]
        for i in range(2, n):
            r.insert(i, (r[i - 1] + r[i - 2]))
    return r


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))