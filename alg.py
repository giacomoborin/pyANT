import math, random

def printif(string,verb= True):
    if verb:
        print(string)

def gcd(m, n):
    if (n == 0):
        return m
    return gcd(n, m % n)


def pollard_p_1(number, bound, stamp=False):
    a = 2
    if stamp:
        print("1 -> a = " + str(a))
    for j in range(2, bound + 1):
        a = pow(base=a, exp=j, mod=number)
        if stamp:
            print(str(j) + " -> a = " + str(a))
    return gcd(a - 1, number)


def pollard_rho(number: int, bound=0, a=1, x0=-1) -> int:
    def f(n: int) -> int:
        return (a + n ** 2) % number

    if bound == 0:
        bound: int = int(math.sqrt(number))
    if x0 == -1:
        x0 = random.randint(0, number)
    y0 = x0
    for j in range(bound):
        y0 = f(f(y0))
        x0 = f(x0)
        if gcd(y0 - x0, number) != 1:
            return gcd(y0 - x0, number)


def fermat_ez(number):
    k = math.isqrt(number) + 1
    h = k ** 2 - number
    i = 0
    while math.isqrt(h) < number / 2:
        print(" k = " + str(k + i) + "^2 : h = " + str(h))
        if h == math.isqrt(h) ** 2:
            return gcd(math.isqrt(number + h) + math.isqrt(h), number)
        h = h + 2 * k + 2 * i + 1
        i += 1


def lucas_W(a, b, R, Q, n, verbose=False):
    yn = b
    xn = a
    if verbose:
        print('Lucas sequence with polynomial f = x^2 - (' + str(R) + ')x + (' + str(Q) + ')')
        print('1: ' + str(a) + ' - 2: '+ str(b) + ' - ', end= '')
    for j in range(2, n):
        yn, xn = R * yn - Q * xn, yn
        if verbose:
            if j == n-1:
                print(j + 1, yn, end=' /', sep=': ')
            else:
                print( j+1 , yn, end = ' - ', sep = ': ')
    return yn

#===============================================
### Quadratic sieve

def odd_res(n):
    while(n%2==0):
        n = n//2
    return (n)

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


#def n_f_sieve(n,bound):


def main():
    return b_smooth_primes(100203)


if __name__ == "__main__":
    print(main())
