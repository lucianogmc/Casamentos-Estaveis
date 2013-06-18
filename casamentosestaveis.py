#!/usr/bin/python 
# -*- coding: latin-1 -*-
import os, sys
import numpy
import random

"""
A fun��o 'ler' l� um arquivo de texto e o transforma em uma matriz do tipo 
numpy.matrix, e em seguida testa as entradas da matriz para verificar se 
correspondem a 2n linhas, cada uma uma permuta��o dos n�meros de 0 a n - 1.

O arquivo de texto deve ter uma �nica linha de texto com o seguinte formato:  
as entradas de uma mesma linha da matriz com espa�os, e as linhas da matriz com 
ponto e v�rgula (';'). Por exemplo, um arquivo com a linha '1 0; 0 1' representa
a matriz identidade de ordem 2.
"""

def ler(arquivo):
    preferencias = open(arquivo, 'r')
    p = numpy.matrix(preferencias.read())

    # Teste de Formato
    [n,m]=p.shape
    if n==2*m:
        # Teste da Soma
        for i in range(n):
            if numpy.sum(p[i]) != m*(m-1)/2:
                print 'Dados n�o compat�veis. Todas as linhas devem ser uma permuta��o de 0, 1, ..., n-1.'
                break
       
        # Teste Principal:    
        else:
             ref = range(n)
             for i in range(n):
                 ref[i] = range(m)
             ref = numpy.matrix(ref)
             arrumacao = numpy.sort(p, axis=1)
             if not (arrumacao == ref).all():
                 print 'Dados n�o compat�veis. Todas as linhas devem ser uma permuta��o de 0, 1, ..., n-1.'
             else:
                 return p
    else:
        print 'Dados n�o compat�veis. Matriz de prefer�ncias deve ter formato 2n por n.'

"""
A fun��o 'converter' � usada para converter uma matriz de prefer�ncias padr�o para 
uma matriz de prefer�ncias adequada ao c�digo do algoritmo principal. Mais detalhes abaixo.
"""
# vamos supor que a matriz j� passou no teste.

def converter(matriz):
    [n,m] = matriz.shape
    A = numpy.copy(matriz)
    for i in range(m):
        for k in range(m):
            A[m+i,matriz[m+i,k]] = k
    return A

"""
A fun��o 'aleatoria' recebe in inteiro positivo n e gera uma matriz de prefer�ncias
 aleat�ria, ou seja, com 2n linhas e n colunas, 
cada linha uma permuta��o de 0, 1, ... , n - 1. Tal matriz � usada para testar 
os algoritmos, e pode ser interpretada tanto como matriz padr�o como tamb�m como 
matriz convertida.
"""
def aleatoria(n):
# Gera matriz aleatoria:
    l=range(2*n)
    for i in range(2*n):
        l[i]=range(n)
        random.shuffle(l[i])
    l = numpy.matrix(l)
    return l

"""
A fun��o 'casamentos' cont�m o algoritmo principal para a obten��o de um casamento
est�vel. Recebe como imput uma matriz 2n x n, cada linha uma permuta��o de 0, 1, 
..., n - 1. As n primeiras linhas representam as mulheres em ordem de preferencia 
para cada homem. J� as n linhas seguintes representam a posi��o de cada homem na 
lista de cada mulher. 
Ou seja, sendo p a matriz, p[k,i] representa a i-�sima mulher da lista do homem k, 
para k de 0 a n-1, e para k de n a 2n-1 representa a posicao do homem numero i na 
lista da mulher n-k.
A fun��o retorna o vetor (lista) h, tal que h[k] representa o n�mero da mulher que 
ser� emparelhada com o homem k.
"""
def casamentos(pref):
    p = numpy.copy(pref)
    n = len(p)/2
    h = [-1]*n # armazena o par de cada homem, h[k] eh o numero da esposa do homem k (-1 significa sem par)
    m = [-1]*n 
    # armazena o par de cada mulher (fun��o inversa de h)

    while sum(h)!=n*(n-1)/2: 
    # testa se todos os homens j� t�m par
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
    # se ela nao esta livre mas prefere o homem k a seu atual par, aceita a proposta.
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
    # este break nao eh necessario, eh apenas uma opcao que parece mais justa; a cada rodada de propostas, cada homem livre faz uma so proposta. Na pr�tica, o resultado obtido � o mesmo com ou sem este break.
    return h

"""
A fun��o 'casamentos1' implementa o algoritmo com uma permuta��o aleat�ria dos
homens para definir a ordem em que prop�em. Pode ser utilizada para observar que o
resultado obtido � sempre o mesmo.
"""
def casamentos1(pref):
    p = numpy.copy(pref)
    n = len(p)/2
    h = [-1]*n # armazena o par de cada homem, h[k] eh o numero da esposa do homem k (-1 significa sem par)
    m = [-1]*n 
    # armazena o par de cada mulher (fun��o inversa de h)

    while sum(h)!=n*(n-1)/2: 
    # testa se todos os homens j� t�m par
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
    # se ela nao esta livre mas prefere o homem k a seu atual par, aceita a proposta.
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
    return h
    
"""
A fun��o 'estabilidade' testa a estabilidade de um determinado emparelhamento.
Recebe dois argumentos, 'h': lista dos n�meros das mulheres emparelhadas com cada
homem, e 'pref': matriz de prefer�ncias considerada j� convertida.
O algoritmo funciona percorrendo, para cada homem i, a lista das mulheres que ele 
prefere a seu atual par, e verificando se cada uma delas prefere seu atual par ao
homem i.
"""
def estabilidade(h,pref):
# Testa a estabilidade de um array de casamentos.
    p = numpy.array(pref)
    n = len(h)
    m=[]
    for i in range(n):
        m.append(h.index(i))
    for i in range(n):
        k = 0
        while p[i,k] != h[i]:
            if p[n+p[i,k], m[p[i,k]]] > p[n+p[i,k],i]:
                print ['instabilidade', i, p[i,k]] # a primeira instabilidade encontrada � impressa na tela.
                break
            else:
                k = k+1
        else:
            continue
        break
    else:
        print 'casamento est�vel!' # caso nenhuma instabilidade seja encontrada.

"""
As duas fun��es a seguir s�o uma comodidade para se fazer o processo completo
com um �nico comando.
"""

# Algoritmo completo a partir de um arquivo, retornando a lista dos pares dos homens:
def casar(arquivo):
    return casamentos(converter(ler(arquivo)))

# Mesmo que o anterior, imprimindo na tela a lista dos pares [homem, mulher]:
def casarp(arquivo):
    lista = casar(arquivo)
    for k in range(len(lista)):
        print [k,lista[k]]
