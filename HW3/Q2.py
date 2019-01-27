def Berlekamp_Massey_algorithm(sequence):
    N = len(sequence)
    s = sequence[:]

    for k in range(N):
        if s[k] == 1:
            break
    f = set([k + 1, 0])  # use a set to denote polynomial
    l = k + 1

    g = set([0])
    a = k
    b = 0

    for n in range(k + 1, N):
        d = 0
        for ele in f:
            d ^= s[ele + n - l]

        if d == 0:
            b += 1
        else:
            if 2 * l > n:
                f ^= set([a - b + ele for ele in g])
                b += 1
            else:
                temp = f.copy()
                f = set([b - a + ele for ele in f]) ^ g
                l = n + 1 - l
                g = temp
                a = b
                b = n - l + 1

    # output the polynomial
    def print_poly(polynomial):
        result = ''
        lis = sorted(polynomial, reverse=False)
        for i in lis:
            if i == 0:
                result += '1'
            else:
                result += 'x^%s' % str(i)

            if i != lis[-1]:
                result += ' + '

        return result

    return (print_poly(f), l)

seq = [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0]
seq.reverse()
(poly, span) = Berlekamp_Massey_algorithm(seq)
seq.reverse()

print 'Input: %s.' % str(seq)
print 'Characteristic Polynomial: (%s),' % poly,
print 'and Linear Span: %d.' % span
