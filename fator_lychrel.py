def fator_lychrel(n):
    """Toma um numero n e retorna o numero de vezes que se precisa somar um numero (comecando por n) a sua forma invertida (lida da direita para a esquerda) para obter- se um numero palindromo. Se apos realizar 50 vezes esse processo um numero palindromo nao for obtido, retorna -1 e esse eh um numero de Lychrel"""

    i = 0 # i eh o contador de quantas vezes o processo para tentar obter um numero palindromo foi executado
    while (i<50) and (n!= int(str(n)[::-1])): # int(str(n)[::-1])) retorna o numero n lido da direita para a esquerda
        sn = int(str(n)[::-1])
        n += sn # a cada ciclo, um numero (comecando pelo n dado como argumento) eh adicionado a sua forma lida da direita para a esquerda, na tentativa de gerar um palindromo
        i += 1 
    if i == 50:
        return -1
    else:
        return i
