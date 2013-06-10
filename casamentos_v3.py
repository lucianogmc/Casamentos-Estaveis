# imput matriz 2n x n, cada linha permutacao de 0..n-1
# n primeiras linhas representam as mulheres em ordem de preferencia para cada 
# homem.
#n linhas seguintes representam a posicao de cada homem na lista de cada mulher.
#ou seja, p(k,i) representa a i-esima mulher da lista do homem k, para k de 0 a n-1
#e para k de n a 2n-1 representa a posicao do homem numero i na lista da mulher n-k.
#programa retorna o vetor (lista) h, tal que h(k) representa o numero da mulher que 
#sera emparelhada com o homem k.
#nesta versao, em vez de considerar a matriz como imput, gera-se uma matriz
#aleatoria, para efeito de testar o algoritmo.
#um programa funcional deveria receber a matriz como imput e testar se cada linha
#eh uma permutacao de 0..n-1.

def aleatoria(n):
# Gera matriz aleatoria:
    import random
    l=range(2*n)
    for i in range(2*n):
        l[i]=range(n)
        random.shuffle(l[i])
    return l

def casamentos(pref):
    import numpy
    p = numpy.copy(pref)
    n = len(p)/2
    h = [-1]*n # armazena o par de cada homem, h[k] eh o numero da esposa do homem k (-1 significa sem par)
    m = [-1]*n 
    # armazena o par de cada mulher (função inversa de h)

    while sum(h)!=n*(n-1)/2: 
    # testa se todos os homens já têm par
        for k in range(n):
            if h[k]==-1: 
    # testa se o homem k esta livre
                for i in range (n):
                    if p[k,i] != -1: 
    # ao longo do processo, a matriz p sera modificada para indicar as propostas ja feitas inserindo entradas -1. esta linha encontra a primeira mulher para a qual o homem k ainda nao propos.
                        if m[p[k,i]]==-1: 
    # se a mulher i da lista do homem k esta livre, aceita a proposta.
                            h[k]=p[k,i]
                            m[h[k]]=k
                            p[k,i] = -1 
                            break 
                        elif p[n+p[k,i], m[p[k,i]]] > p[n+p[k,i],k]: 
    #se ela nao esta livre mas prefere o homem k a seu atual par, aceita a proposta.
                            h[m[p[k,i]]] = -1
                            h[k]=p[k,i]
                            m[h[k]]=k
                            p[k,i] = -1
                            break 
    # este break, assim como o anterior, sao necessarios para que o homem k, agora casado, pare de propor.
                        else: 
    # caso contrario a proposta eh recusada.
                            p[k,i] = -1
                            break 
    # este break nao eh necessario, eh apenas uma opcao que parece mais justa; a cada rodada de propostas, cada homem livre faz uma so proposta.
    return h

def casamentos1(pref):
    import numpy
    p = numpy.copy(pref)
    n = len(p)/2
    h = [-1]*n # armazena o par de cada homem, h[k] eh o numero da esposa do homem k (-1 significa sem par)
    m = [-1]*n 
    # armazena o par de cada mulher (função inversa de h)

    while sum(h)!=n*(n-1)/2: 
    # testa se todos os homens já têm par
        ordem = range(n)
        random.shuffle(ordem)
        for k in ordem:
            if h[k]==-1: 
    # testa se o homem k esta livre
                for i in range (n):
                    if p[k,i] != -1: 
    # ao longo do processo, a matriz p sera modificada para indicar as propostas ja feitas inserindo entradas -1. esta linha encontra a primeira mulher para a qual o homem k ainda nao propos.
                        if m[p[k,i]]==-1: 
    # se a mulher i da lista do homem k esta livre, aceita a proposta.
                            h[k]=p[k,i]
                            m[h[k]]=k
                            p[k,i] = -1 
                            break 
                        elif p[n+p[k,i], m[p[k,i]]] > p[n+p[k,i],k]: 
    #se ela nao esta livre mas prefere o homem k a seu atual par, aceita a proposta.
                            h[m[p[k,i]]] = -1
                            h[k]=p[k,i]
                            m[h[k]]=k
                            p[k,i] = -1
                            break 
    # este break, assim como o anterior, sao necessarios para que o homem k, agora casado, pare de propor.
                        else: 
    # caso contrario a proposta eh recusada.
                            p[k,i] = -1
                            #break 
    # este break nao eh necessario, eh apenas uma opcao que parece mais justa; a cada rodada de propostas, cada homem livre faz uma so proposta.
    return h
    

def estabilidade(h,pref):
# Testa a estabilidade de um array de casamentos.
    import numpy
    p = numpy.array(pref)
    n = len(h)
    m=[]
    for i in range(n):
        m.append(h.index(i))
    for i in range(n):
        k = 0
        while p[i,k] != h[i]:
            if p[n+p[i,k], m[p[i,k]]] > p[n+p[i,k],i]:
                print ['instabilidade', i, p[i,k]]
                break
            else:
                k = k+1
        else:
            continue
        break
    else:
        print 'casamento estável!'

