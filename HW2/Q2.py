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
gen = []
cp = []
for i in range(1, 46):
    d = gcd(i,46)
    if d == 1:
        cp.append(i)
length = len(cp)

for k in range(0,length):
    gen_k = []
    for m in range(1,length+1):
        t = cp[k]**m % 46
        if t not in gen_k:
            t = cp[k]**m % 46
            gen_k.append(t)
        #print(t)
    gen_k.sort()
    if len(gen_k) == len(cp):
        gen.append(cp[k])
    print "For", cp[k], "=", gen_k, "# of elements: ", len(gen_k)
gen.sort()
#print len(cp)
#print cp
print "\n", "# of elements in Z46*: ", len(cp)
print "Elements in Z46*: ", cp
print "\n", "# of generators in Z46*: ", len(gen)
print "Generators :", gen

qr = []
for r in range(0,length):
    q = cp[r]**2 % 46
    if q not in qr:
        qr.append(q)
    qr.sort()
print "\n", "# of elements in Q46*: ", len(qr)
print "Elements in Q46*: ", qr

gen2 = []
for z in range(0,len(qr)):
    gen_z = []
    for n in range(1,len(qr)+1):
        e = qr[z]**n % 46
        if e not in gen_z:
            gen_z.append(e)
    gen_z.sort()
    if len(gen_z) == len(qr):
        gen2.append(qr[z])
    print "For", qr[z], "=", gen_z, "# of elements: ", len(gen_z)
gen2.sort()
print "\n", "# of generators in Q46*: ", len(gen2)
print "Generators :", gen2
