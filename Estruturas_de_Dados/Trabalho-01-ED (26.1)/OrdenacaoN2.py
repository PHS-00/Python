"""
Arquivo Python para inserção de códigos de algoritmos de ordenação O(n^2)
autor: Arthur Souza
"""

def bubbleSortIterativo(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista


def bubbleSortRecursivo(lista, n=None):
    if n is None:
        n = len(lista)

    if n == 1:
        return lista

    for i in range(n - 1):
        if lista[i] > lista[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]

    return bubbleSortRecursivo(lista, n - 1)


def ordenarIterativoN2(lista):
    '''
    Incluir código do algoritmo de ordenação iterativo O(n^2)
    '''
    return bubbleSortIterativo(lista)


def ordenarRecursivoN2(lista):
    '''
    Incluir código do algoritmo de ordenação recursiva O(n^2)
    '''
    return bubbleSortRecursivo(lista)