from collections import deque

# C(x) = 1 + x^2 + x^3 + x^5 + x^6 (011011)
# Initial Step = 000001
# Maximum Period = 63 (2^6 - 1)

def LFSR(sequence):
    x = deque(sequence)
    y = []
    z = x[5] ^ x[4] ^ x[2] ^ x[1]    # Connection Polynomial = x^6 + x^5 + x^3 + x^2 + 1 (BMA)
    k = x[5]                         # Initial Step 000001
    x.rotate(1)
    x[0] = z
    return x

x = []
y = []
sequence = deque([0,0,0,0,0,1])

for i in range(1, 127):
    sequence = LFSR(sequence)
    s = list(sequence)
    # print i, sequence
    if s not in x:
        x.append(s)
        print i, "\t", s
    elif s not in y:
        y.append(s)
if x == y:
    print "\n", "Period is 2^6 - 1 which means connection polynomial generates maximum length sequences"
