import math
#useless stuff
def printif(string,verb= True):
    if verb:
        print(string)


#===============================================
### Quadratic sieve

def odd_res(n):
    while(n%2==0):
        n = n//2
    return (n)

def res_p(n,p):
    while (n % p == 0):
        n = n // p
    return (n)

def v_p(n,p):
    v = 0
    while (n % p == 0):
        n = n // p
        v += 1
    return (v)

def v_res_p(n,p):
    v = 0
    while (n % p == 0):
        n = n // p
        v += 1
    return [v,n]

def two_k(c,p):
    k = 0
    c = c % p
    while(c != p-1):
        k += 1
        c = pow(c, 2, p)
    return k

def non_quad(p):
    for g in range(2,p-1):
        if pow(g , (p-1)//2 , p)== p-1:
            return g
    return


#def legendre_qs()

#assuming that p does not divide a, otherwhise it's easy
def solve_quad(a, p, verbose = False):
    if pow(a , (p-1)//2 , p) != 1:
        printif('No solutions',verbose)
        return []
    printif('Two solutions', verbose)
    m = p % 4
    # find g non quad
    g = non_quad(p)
    if m == 3:
        x = pow(a, (p+1)//4, p )
        return [x, p-x]
    elif m == 1:
        q = odd_res(p-1)
        z = pow(g, q, p)
        b = pow(a, ((q+1)//2), p)
        c = pow(a, q, p)
        while c != 1:
            k = two_k(c, p)
            l = two_k(z, p)
            b = (b * pow(z, int(pow(2, l - k - 1)), p)) % p
            c = (c * pow(z, pow(2, l - k), p)) % p
            z = pow(z, pow(z, pow(2, l - k)), p)
        return [b, p-b]
    else:
        print('sei scemo?')

def li(n):
    return math.ceil(n/math.log(n))

def b_smooth_primes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    from itertools import compress
    return [i for i in range(len(prime)) if prime[i]]
#    return list(compress(range(len(prime)), prime))

