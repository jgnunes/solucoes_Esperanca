def ligacoes(n,l):
    """Retorna uma lista com a quantidade de ligacoes que cada um dos n vendedores executou, dada uma lista l com o tempo de duracao de cada ligacao"""

    # lida com o caso onde nao ha vendedor algum para executar as ligacoes, ou seja, n = 0
    if n == 0:
        print ("Sem vendedores, nenhuma ligacao feita")

    # lida com os casos onde ha vendedores para fazer as ligacoes 
    else:
        lf = [0]*n # criar uma lista lf com o numero de ligacoes feitas por cada vendedor

        # lida com o caso onde o numero de vendedores eh maior que o numero de ligacoes a serem feitas
        if n >= len(l):
            for i in range (len(l)):
                lf[i] += 1
                
        l = [5, 3, 4, 10, 11, 6]
        n = 3
        lp = [5, 3, 4]
        l = [10, 11, 6]
        
        lp = [5-3,10, 4-3]
        lp = [2, 10, 1]
        l = [11 , 6]
        
        
        # lida com o caso onde o numero de ligacoes a serem feitas eh maior que o numero de vendedores
        else:
            lp= l[:n] # cria uma lista parcial (lp) que contem os tempos das chamadas que estao sendo executadas por cada vendedor
            lf= [1]*n # como o numero de ligacoes eh maior que o de vendedores, cada vendedor vai realizar, no minimo, uma ligacao
            del l[:n] # deleta as n primeiras chamadas da lista que contem os tempos de chamadas
            while len(l) != 0:
                m = lp.index(min(lp)) # m sera o indice do vendedor que ficara livre primeiro para fazer a proxima ligacao
                lf[m] +=1 # assim que o vendedor fica livre, executa uma nova ligacao. O numero de ligacoes executadas por ele deve ser acrescido de 1
                # esse comando for atualiza os valores da lista parcial para o proximo round de decisao sobre quem sera o vendedor a ficar livre primeiro
                for j in range(len(lp)):
                    if j == m:
                        lp[j] = l[0] # este eh o vendedor que iniciou a ligacao neste round. Ele ficara livre apos decorrido o tempo da ligacao que acabou de iniciar
                    else:
                        lp[j] -= min(lp) # estes sao os vendedores que nao iniciaram ligacoes neste round. Eles ficaram livres passado o tempo da ligacao que ele tinha se proposto a executar menos o tempo da ligacao executada pelo vendedor que iniciou a ligacao neste round
                del l[0] # deleta, da lista de ligacoes a serem feitas, aquela ligacao que foi iniciada neste round (que sempre sera a primeira da lista)
        return lf
