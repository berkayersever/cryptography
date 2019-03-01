from fractions import gcd
from random import randint

e = 65537
n = 140551657748123311843904632833471669259677424177527429472076641459146867906661942068298379563181123587514898171198345842702518087577996533400370831952801883330035838563895672878817032429070070491801818686348972449259014970161691017147789125584023630380720107022841065881140401317726964037566281222748970712203
c = 107370145208181012882157035957831285007639861193502148958526088911145111312354857879651315298430491706057927363584703699650832365083149730388058817716227351580643780596923032021272650197705800013301435840379066513203705883311188119667109083477935129425038367472101389436165688559837901078746430028139353590988
r = 293983510760590056330647711733834136168
m2 = 120402034061049960628218111909711136793099013099107787057903748477267562993246581824333179810106790393644009529285482451478168014966790953995488737879898316885941253266903643015596143055400220581436351563090027302223659679590697117170241040607927681665138200749531346830851443691882051320372085132068789965278

# x = randint(pow(2, 64, n),pow(2, 128, n))   # Random Number

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


# print "x:", x
print "m':", m2                     # Query from the Oracle

c2 = (c * pow(r, e, n)) % n
print "c':", c2

m = (m2 * modinv(r,n)) % n
print "m:", m