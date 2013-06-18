#!/usr/bin/python 
# -*- coding: latin-1 -*-
import os, sys
import numpy
import random

"""
A função 'ler' lê um arquivo de texto e o transforma em uma matriz do tipo 
numpy.matrix, e em seguida testa as entradas da matriz para verificar se 
correspondem a 2n linhas, cada uma uma permutação dos números de 0 a n - 1.

O arquivo de texto deve ter uma única linha de texto com o seguinte formato:  
as entradas de uma mesma linha da matriz com espaços, e as linhas da matriz com 
ponto e vírgula (';'). Por exemplo, um arquivo com a linha '1 0; 0 1' representa
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
                print 'Dados não compatíveis. Todas as linhas devem ser uma permutação de 0, 1, ..., n-1.'
                break
       
        # Teste Principal:    
        else:
             ref = range(n)
             for i in range(n):
                 ref[i] = range(m)
             ref = numpy.matrix(ref)
             arrumacao = numpy.sort(p, axis=1)
             if not (arrumacao == ref).all():
                 print 'Dados não compatíveis. Todas as linhas devem ser uma permutação de 0, 1, ..., n-1.'
             else:
                 return p
    else:
        print 'Dados não compatíveis. Matriz de preferências deve ter formato 2n por n.'

"""
A função 'converter' é usada para converter uma matriz de preferências padrão para 
uma matriz de preferências adequada ao código do algoritmo principal. Mais detalhes abaixo.
"""
# vamos supor que a matriz já passou no teste.

def converter(matriz):
    [n,m] = matriz.shape
    A = numpy.copy(matriz)
    for i in range(m):
        for k in range(m):
            A[m+i,matriz[m+i,k]] = k
    return A

"""
A função 'aleatoria' recebe in inteiro positivo n e gera uma matriz de preferências
 aleatória, ou seja, com 2n linhas e n colunas, 
cada linha uma permutação de 0, 1, ... , n - 1. Tal matriz é usada para testar 
os algoritmos, e pode ser interpretada tanto como matriz padrão como também como 
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
A função 'casamentos' contém o algoritmo principal para a obtenção de um casamento
estável. Recebe como imput uma matriz 2n x n, cada linha uma permutação de 0, 1, 
..., n - 1. As n primeiras linhas representam as mulheres em ordem de preferencia 
para cada homem. Já as n linhas seguintes representam a posição de cada homem na 
lista de cada mulher. 
Ou seja, sendo p a matriz, p[k,i] representa a i-ésima mulher da lista do homem k, 
para k de 0 a n-1, e para k de n a 2n-1 representa a posicao do homem numero i na 
lista da mulher n-k.
A função retorna o vetor (lista) h, tal que h[k] representa o número da mulher que 
será emparelhada com o homem k.
"""
def casamentos(pref):
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
    # este break nao eh necessario, eh apenas uma opcao que parece mais justa; a cada rodada de propostas, cada homem livre faz uma so proposta. Na prática, o resultado obtido é o mesmo com ou sem este break.
    return h

"""
A função 'casamentos1' implementa o algoritmo com uma permutação aleatória dos
homens para definir a ordem em que propõem. Pode ser utilizada para observar que o
resultado obtido é sempre o mesmo.
"""
def casamentos1(pref):
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
A função 'estabilidade' testa a estabilidade de um determinado emparelhamento.
Recebe dois argumentos, 'h': lista dos números das mulheres emparelhadas com cada
homem, e 'pref': matriz de preferências considerada já convertida.
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
                print ['instabilidade', i, p[i,k]] # a primeira instabilidade encontrada é impressa na tela.
                break
            else:
                k = k+1
        else:
            continue
        break
    else:
        print 'casamento estável!' # caso nenhuma instabilidade seja encontrada.

"""
As duas funções a seguir são uma comodidade para se fazer o processo completo
com um único comando.
"""

# Algoritmo completo a partir de um arquivo, retornando a lista dos pares dos homens:
def casar(arquivo):
    return casamentos(converter(ler(arquivo)))

# Mesmo que o anterior, imprimindo na tela a lista dos pares [homem, mulher]:
def casarp(arquivo):
    lista = casar(arquivo)
    for k in range(len(lista)):
        print [k,lista[k]]
