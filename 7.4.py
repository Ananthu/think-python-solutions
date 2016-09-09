

import math


def newtons(n):
    n = float(n)  # convert input to float so printout() doesn't have to
    x = n / 2  # rough estimate
    i = 0
    while i < 10:
        y = (x + n / x) / 2  # newtons method
        x = y
        i += 1
    return y


def libmath(n):
    n = float(n)
    return math.sqrt(n)


def printout():
    print '{:<12}\t{:<12}\t{}'.format('newtons', 'libmath', 'delta')
    for i in range(1, 10):
        n = newtons(i)
        l = libmath(i)
        ab = abs(n - l)
        print '{:<12}\t{:<12}\t{}'.format(n, l, ab)

printout()
