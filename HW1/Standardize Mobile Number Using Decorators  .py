def wrapper(f):
    def fun(l):
        f('+91 {} {}'.format(i[-10:-5], i[-5:]) for i in l)

    return fun


def wrapper(f):
    def phone(l):
        f(["+91 " + c[-10:-5] + " " + c[-5:] for c in l])

    return phone