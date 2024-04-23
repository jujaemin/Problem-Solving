import sys
from fractions import Fraction

T = int(sys.stdin.readline())

for _ in range(T):
    a,b = map(int, sys.stdin.readline().split())
    while a != 1:
        x = int(b//a)+1
        a = a*x-b
        b *= x
        a, b = map(int, str(Fraction(a,b)).split('/'))
    print(b)