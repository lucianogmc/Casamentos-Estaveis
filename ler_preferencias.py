"""
Este código lê um arquivo de texto e o transforma em uma matriz do tipo numpy.matrix,
e em seguida testa as entradas da matriz para verificar se correspondem a 2n linhas,
cada uma uma permutação dos números de 0 a n - 1.

O arquivo de texto deve ter o seguinte formato: uma única linha de texto separando as entradas da matriz com espaços e as linhas da matriz com ponto e vírgula (';').
"""

def ler(arquivo):
    import numpy
    preferencias = open(arquivo, 'r')
    p = numpy.matrix(preferencias.read())

    #Teste de Formato
    [n,m]=p.shape
    if n==2*m:
        #Teste da Soma
        for i in range(n):
            if numpy.sum(p[i]) != m*(m-1)/2:
                print 's Dados não compatíveis. Todas as linhas devem ser uma permutação de 0, 1, ..., n-1.'
                break
            
        else:
             ref = range(n)
             for i in range(n):
                 ref[i] = range(m)
             ref = numpy.matrix(ref)
             arrumacao = numpy.sort(p, axis=1)
             if not (arrumacao == ref).all():
                 print 'p Dados não compatíveis. Todas as linhas devem ser uma permutação de 0, 1, ..., n-1.'
             else:
                 return p
    else:
        print 'Dados não compatíveis. Matriz de preferências deve ter formato 2n por n.'
