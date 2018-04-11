from perimetro import perimetro
from comprimento import comprimento
from math import sqrt

def area(p, q, r):
    s = (perimetro(p, q, r))/2.0
    a = comprimento(p, q)
    b = comprimento(p, r)
    c = comprimento(q, r)
    area = sqrt(s*(s-a)*(s-b)*(s-c))
    return area

if __name__ == "__main__":
    print(area([0,1],[2,4],[-7,3]))