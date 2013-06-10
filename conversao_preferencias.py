"""
Código para converter uma lista de preferências padrão para uma lista de preferências
adequada ao código do algoritmo principal.
"""
# vamos supor que a matriz já passou no teste.

def converter(matriz):
    import numpy
    [n,m] = matriz.shape
    A = numpy.copy(matriz)
    for i in range(m):
        for k in range(m):
            A[m+i,matriz[m+i,k]] = k
    return A

#não funciona.

# Vamos fazer primeiro com uma lista:

def convertlist(lista):
    convertida = []
    for i in range(len(lista)):
        convertida.append(lista.index(i))
    return convertida

#lista de listas:

def convll(listal):
    convertida = []
    for k in range(len(listal)):
        convertida.append(convertlist(listal[k]))
    return convertida

