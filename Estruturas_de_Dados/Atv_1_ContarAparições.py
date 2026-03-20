import os

# Função para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

limpar_tela()

# Atividade 01: Considere uma função que recebe dois parâmetros:
#   1. Lista com n elementos
#   2. Elemento para pesquisar na lista
# A função deve percorrer a lista e calcular a quantidade de vezes que o elemento aparece na lista.
# a) Implemente a função
# b) Calcule o tempo de execução, conforme o modelo RAM 

def contar_aparicoes(lista, pesquisa):
    contador = 0
    for i in lista:
        if i == pesquisa:
            contador += 1
    return contador

print(contar_aparicoes([1, 1, 1, 1, 2], 1))

input()

# Atividade 02: Considere uma função que recebe uma lista como parâmetro.
#   1. Lista com n elementos
# A função deve percorrer a lista, identificar os elementos repetidos e retornar uma lista com os elementos que se repetem.
# a) Implemente a função
# b) Calcule o tempo de execução, conforme o modelo RAM 

limpar_tela()

def listar_repetidos(lista):
    repetidos = []
    for i in range(len(lista)):
        if lista[i] in lista[i+1:] and lista[i] not in repetidos:
            repetidos.append(lista[i])

    return repetidos

print(listar_repetidos([1, 1, 1, 1, 2, 2, 3]))

input()