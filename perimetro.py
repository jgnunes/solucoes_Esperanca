#from nomeDoArquivo import funcao
from comprimento import comprimento

def perimetro(p, q, r):
    l1 = comprimento(p, q)
    l2 = comprimento(p, r)
    l3 = comprimento(q, r)
    perimetro = l1 + l2 + l3
    return perimetro

if __name__ == "__main__":
    print(perimetro([6,8],[1,-4],[6,-4]))