import sys
import math

T = int(sys.stdin.readline())

def extended_euclid(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1

    while b != 0:
        k, a, b = a//b, b, a%b
        x0, x1 = x1, x0-(k*x1)
        y0, y1 = y1, y0-(k*y1)
    
    return x0, y0

for _ in range(T):
    M, N, x, y = map(int, sys.stdin.readline().split())
    gcd = math.gcd(M,N)
    if x%gcd != y%gcd:
        print(-1)
    else:
        m, n = M//gcd, N//gcd
        p, q = extended_euclid(m, n)
        result = (x*q*n)+(y*p*m)
        lcm = math.lcm(M, N)
        if int(result%lcm) == 0:
            print(result)
        else:
            print(int(result%lcm))