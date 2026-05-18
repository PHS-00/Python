"""
Arquivo Python para inserção de códigos de algoritmos de ordenação O(n*Log(n))
autor: Arthur Souza
"""

def merge(esquerda, direita):
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado


def mergeSortRecursivo(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = mergeSortRecursivo(lista[:meio])
    direita = mergeSortRecursivo(lista[meio:])

    return merge(esquerda, direita)


def mergeSortIterativo(lista):
    largura = 1
    n = len(lista)

    while largura < n:
        for i in range(0, n, 2 * largura):
            esquerda = lista[i:i+largura]
            direita = lista[i+largura:i+2*largura]
            lista[i:i+2*largura] = merge(esquerda, direita)

        largura *= 2

    return lista


def ordenarIterativoNLog(lista):
    '''
    Incluir código do algoritmo de ordenação iterativo O(n*Log(n))
    '''
    return mergeSortIterativo(lista)


def ordenarRecursivoNLog(lista):
    '''
    Incluir código do algoritmo de ordenação recursiva O(n*Log(n))
    '''
    return mergeSortRecursivo(lista)