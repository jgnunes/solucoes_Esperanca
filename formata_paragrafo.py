def formata_paragrafo(texto, n):
    palavras = texto.split() #cria uma lista com todas as palavras do texto
    linhas = [] #inicia a lista que ira conter todas as linhas do paragrafo formatado
    contador_caracteres = 0 #inicia um contador de numero de caracteres 
    linha = [] #inicia a lista que ira conter o conjunto de palavras de uma dada linha
    for palavra in palavras: #itera sobre cada palavra do texto
        if len(linha) == 0: #se nao existe nenhuma palavra na linha, entao simplesmente o comprimento da palavra ao contador de caracteres
            contador_caracteres += len(palavra)
        else: #se ja existe alguma palavra na linha, adicionamos o comprimento da palavra mais 1, representando um espaco que tem que existir entre cada palavra
            contador_caracteres += (len(palavra) + 1)
        if contador_caracteres <= n: #se o numero de caracteres da linha atual eh menor ou igual limite n, adicionamos a palavra na linha
            linha.append(palavra)
        else: #se o numero de caracteres for maior que o limite, nao adicionamos a palavra na linha mas sim criamos uma nova linha onde o primeiro elemento sera a palavra da iteracao atual
            linhas.append(linha)
            linha = [palavra]
            contador_caracteres = len(palavra)
    linhas.append(linha)

    for linha in linhas[:-1]: #formata todas as linhas (menos a ultima), adicionando o numero de espacos necessarios para alcancar a quantidade de caracteres n determinada pelo input
        comprimento_linha = len("".join(linha))
        espacos_a_adicionar = n - comprimento_linha #calcula numero de espacos a serem adicionados para atingir a quantidade de caracteres n
        if len(linha) == 1: #se a linha tem apenas uma palavra, os espacos de formatacao sao adicionados a direita desta palavra
            espacos_a_cada_palavra = espacos_a_adicionar
            for i in range(len(linha)):
                linha[i] += " "*espacos_a_adicionar
        else: #se a linha tem mais de uma palavra, ao menos um espaco eh adicionado entre cada palavra, e os outros espacos sao adicionados de forma ao comprimento da linha atingir n caracteres 
            espacos_a_cada_palavra = espacos_a_adicionar//(len(linha)-1) #em python3, a divisao entre inteiros eh com duas barras (//); em python2, apenas uma
            espacos_extras = espacos_a_adicionar%(len(linha)-1)
            for i in range(len(linha)):
                if i == 0:
                    linha[i] += " "*(espacos_a_cada_palavra+espacos_extras)
                elif i != len(linha)-1:
                    linha[i] += " "*espacos_a_cada_palavra
    
                  
    if len(linhas[-1]) > 1: #lida com o caso onde a ultima linha contem mais de uma palavra  
        for i in range(len(linhas[-1])): #itera sobre cada palavra, adicionando espacos entre cada uma
            if i != len(linhas[-1]) - 1:
                linhas[-1][i] += " "
                
    for i in range(len(linhas)): #transforma cada linha (que ate o momento era uma lista de strings) em uma string unica
        linhas[i] = "".join(linhas[i])

    return linhas

