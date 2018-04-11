from domina import domina

# l = [[0,1],[0,0],[4,8]]
# l = [[0,1],[0,0]]

# a = [1,5]
# b = [5,1]

def independentes(l):
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if not domina(l[i], l[j]) and not domina(l[j], l[i]):
                return True
    return False

if __name__ == "__main__":
    l_independente = [[0,1],[1,0],[2,2]] # nem [0,1] domina [1,0] nem [1,0] domina [0,1], portanto sao independentes
    l_dependente = [[0,0],[2,2],[3,3]] # [2,2] domina [0,0] e [3,3] domina [2,2] e [0,0], portanto nao ha pares de pontos independentes
    print(independentes(l_independente))
    print(independentes(l_dependente))
