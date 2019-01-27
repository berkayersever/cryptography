from fractions import gcd
import math

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


#Part a
n = 120032070747790791430008804988
a = 7211941535834517096225500817
b = 102092299425228521972149597163

#Part b
#n = 120032070747790791430008804988
#a = 44575693167043501900449109190
#b = 84664078284205068314514580089

#Part c
#n = 120032070747790791430008804988
#a = 404
#b = 2124884389680246530198080982220

if gcd(a,n) == 1:
    print "There is exactly one solution. gcd(a,n) = 1"
    aI = modinv(a,n)
    x = (aI * b) % n
    print "a':", aI
    print "x:", x
else:
    d = gcd(a,n)
    if b % d == 0:
        print "There are exactly", d, "solutions"
        aI = modinv((a/d),(n/d))
        xI = (aI * (b/d)) % (n/d)
        for i in range(0,d):
            x = xI + (i*(n/d))
            print "x", i+1,":", x
    elif b % d != 0:
        print "There is NO solution. Because d doesn't divide b"
        print "Remainder:", (b % d)
