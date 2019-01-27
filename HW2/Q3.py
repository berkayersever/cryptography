from fractions import gcd
import math
import timeit
import time

p  = 12997110888321186459316436989724265349460712629389513072528028592113499927549315535209275673470089822303733552137264381101263928058260190003283395786606613
q  = 12208677561088985820124024567796306546470708824672729385334541873189398794633650052335324309711480763919028490727764288604694220087933148985261608483250761
m1 = 104508383527831908823036869386648261753406819764116432937577039021334848453871469297253914394880121355608067237189088530241064709118310089323613713098921642285063603825756456138538154719968501891170428872546150841926912027053577225264111903314505091217903294998448178692295392732881494063202944747727969714684
e  = 67
n  = p * q
c  = pow(m1, e, n)



print "n:", n, "\n", "c:", c
print(c)

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

def phi(n):
    amount = 0

    #for k in range(1, n + 1):
    for k in xrange (3, int(n**0.5)+1, 2):
        if fractions.gcd(n, k) == 1:
            amount += 1
    return amount

w = (p-1)*(q-1)
print "phi(n):", w

d = modinv(e,w)
print "d:", d

m2 = pow(c, d, n)
print "m':", m2

if m1 == m2:
    print "m = m'"
else:
    print "m != m'"

# Part c
m3 = pow(c, d, p)
m4 = pow(c, d, q)

qI = modinv(q,p)
pI = modinv(p,q)

CRT = ((m3*q*qI) + (m4*p*pI)) %n
print "CRT:", CRT

if m2 == CRT:
    print "m2 = CRT :)"
else:
    print "m2 != CRT :("

#Part d
print "\n","Part d"

iter = 100
t1 = time.clock()
for i in range(0, iter):
    pow(c, d, n)
t2 = time.clock()
print "Exponentiation time in part b:", t2-t1


t3 = time.clock()
for i in range(0, iter):
    ((pow(c, d, p)*q*qI) + (pow(c, d, q)*p*pI)) %n
t4 = time.clock()
print "Exponentiation time in part c:", t4-t3

if (t2-t1) < (t4-t3):
    print "b wins the race"
elif (t2-t1) > (t4-t3):
    print "CRT wins the race"
else:
    print "Draw"

cp = c % p
print "cp:", cp
cq = c % q
print "cq:", cq
dp = d % (p-1)
print "dp:", dp
dq = d % (q-1)
print "dq:", dq
print "p':", modinv(p,q)
print "q':", modinv(q,p)
print "cp^dp:", pow(cp, dp, p)
print "cq^dq:", pow(cq, dq, q)
