from fractions import gcd
from collections import Counter

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

w = []

p = 3
q = 5
n = p * q

for x in range(1, 15):
    h = pow(x, 2, n)
    print "x:", x, "\t", "H(x) = ", h
    w.append(h)

print "\n", Counter(w)
