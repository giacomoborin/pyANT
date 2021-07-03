import math, random
import pandas

def printif(string,verb = True):
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

def poll_rho_diag(p: int, a = 1):
    def f(n: int) -> int:
        return (a + n ** 2) % p
    def poll_conv(x0):
        x = [x0]
        xi = x0
        conv1 = False
        conv2 = False
        while (not conv1):
            xi = f(xi)
            for j in range(len(x)):
                if x[j]==xi:
                    conv1=True
                    n, nd = j, len(x)
                    break
            x.append(xi)
        t=0
        xi = x0
        x2i = x0
        while not conv2:
            xi = f(xi)
            x2i = f(f(x2i))
            t += 1
            if xi == x2i:
                break
        return [x0, n, nd, t]
    return [poll_conv(x0) for x0 in range(p)]



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



#def n_f_sieve(n,bound):


def main():
    return poll_rho_diag(13)


if __name__ == "__main__":
    print(pandas.DataFrame(main()))
