from math import acos, degrees
from comprimento import comprimento

def angulos(p, q, r):
    a = comprimento(p, q)
    b = comprimento(p, r)
    c = comprimento(q, r)
    A = acos(((c**2) + (b**2) - (a**2))/(2*c*b))
    B = acos(((a**2) + (c**2) - (b**2))/(2*a*c))
    C = acos(((a**2) + (b**2) - (c**2))/(2*a*b))

    A = degrees(A)
    B = degrees(B)
    C = degrees(C)

    return [A, B, C]

if __name__ == "__main__":
    print(angulos([0,0],[10,0],[5,8.66]))
