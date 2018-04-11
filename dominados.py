from domina import domina

# l = [[0,1],[0,0],[4,8]]
# p = [3,3]

def dominados(l, p):
    dominados = []
    for ponto in l:
        if domina(p, ponto):
            dominados.append(ponto)
    return dominados

if __name__ == "__main__":
    print(dominados([[0,1],[0,0],[4,8]], [3,3]))