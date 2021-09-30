import math


# useless stuff
def printif(string, verb=True):
    if verb:
        print(string)


# ===============================================
### Quadratic sieve

def odd_res(n):
    while (n % 2 == 0):
        n = n // 2
    return (n)


def res_p(n, p):
    while (n % p == 0):
        n = n // p
    return (n)


def v_p(n, p):
    v = 0
    while (n % p == 0):
        n = n // p
        v += 1
    return (v)


def v_res_p(n, p):
    v = 0
    while (n % p == 0):
        n = n // p
        v += 1
    return [v, n]


def two_k(c, p):
    k = 0
    c = c % p
    while (c != p - 1):
        k += 1
        c = pow(c, 2, p)
    return k


def non_quad(p):
    for g in range(2, p - 1):
        if pow(g, (p - 1) // 2, p) == p - 1:
            return g
    return


def legendre_qs(n, p):
    return pow(n, (p - 1) // 2, p)


# assuming that p does not divide a, otherwhise it's easy
def solve_quad(a, p, verbose=False, prime_out=False):
    if pow(a, (p - 1) // 2, p) != 1:
        printif('No solutions', verbose)
        return []
    printif('Two solutions', verbose)
    m = p % 4
    # find g non quad
    g = non_quad(p)
    if m == 3:
        x = pow(a, (p + 1) // 4, p)
        if prime_out:
            return [p, x, p - x]
        return [x, p - x]
    elif m == 1:
        q = odd_res(p - 1)
        z = pow(g, q, p)
        b = pow(a, ((q + 1) // 2), p)
        c = pow(a, q, p)
        while c != 1:
            k = two_k(c, p)
            l = two_k(z, p)
            b = (b * pow(z, int(pow(2, l - k - 1)), p)) % p
            c = (c * pow(z, pow(2, l - k), p)) % p
            z = pow(z, pow(z, pow(2, l - k)), p)
        if prime_out:
            return [p, b, p - b]
        return [b, p - b]
    elif p == 2:
        if prime_out:
            return [2, 1, 1]
        return [1, 1]
    else:
        print('sei scemo? stai usando il primo ', p)


def li(n):
    return math.ceil(n / math.log(n))


def sq_ceil(n):
    return math.ceil(math.sqrt(n))


# this function return an array with all the primes < n
def b_smooth_primes(b):
    prime = [True for _ in range(b + 1)]
    p = 2
    while (p * p <= b):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * 2, b + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    #    from itertools import compress
    return [i for i in range(len(prime)) if prime[i]]


#    return list(compress(range(len(prime)), prime))

def b_primes_qres(n, b):
    r = [solve_quad(n, p, prime_out=True) for p in b_smooth_primes(b)]
    return [v for v in r if v]


def q_sieve(n, b, M):
    def f(i):
        return (i + sq_ceil(n)) ** 2 - n

    f = [f(i) for i in range(M)]
    sieve = f.copy()
    vp = b_primes_qres(n, b)
    pp = [v[0] for v in vp]
    for v in vp:
        # I find a solution to the equation f(i)=0 mod p using Tonelli-Shanks
        i = (v[1] - sq_ceil(n)) % v[0]
        # I divide by p ( = v[0] ) the ones that are divisible
        for j in range(i, M, v[0]):
            sieve[j] = res_p(sieve[j], v[0])
        if v[1] != v[2]:
            i = (v[2] - sq_ceil(n)) % v[0]
            for j in range(i, M, v[0]):
                sieve[j] = res_p(sieve[j], v[0])
    A = [[i + sq_ceil(n), f[i]] + [v_p(f[i], p) % 2 for p in pp] for i in range(M) if sieve[i] == 1]
    return A


# Continua ad: https://handwiki.org/wiki/Quadratic_sieve

if __name__ == '__main__':
    print('q_sieve_alg.py loaded')
    # print(q_sieve(15347,30,100))
