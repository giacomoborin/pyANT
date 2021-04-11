import math, random


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
    i=0
    while math.isqrt(h) < number/2:
        print(" k = " + str(k + i) + "^2 : h = " + str(h))
        if h == math.isqrt(h) ** 2:
            return gcd(math.isqrt(number + h) + math.isqrt(h), number)
        h = h + 2*k + 2*i + 1
        i += 1


def main():
    return gcd(9,8)

if __name__ == "__main__":
    print(main())