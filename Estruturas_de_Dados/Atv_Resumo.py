import os

# Função para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

limpar_tela()

# Conceituais

# Questão 01. Qual a principal diferença entre uma Lista e uma Tupla ?
# A lista é editável, o que significa que podemos alterar, adicionar e remover itens de uma lista depois de ela ter sido criada.
# As tuplas são imutáveis, o que significa que não podemos alterar, adicionar ou remover itens depois que a tupla tiver sido criada.

# Questão 02. Se você converter a lista [10, 20, 20, 30, 40, 40] em um Set, qual será o resultado final? Explique por que isso ocorre.
limpar_tela()
lista = [10, 20, 20, 30, 40, 40]
conjunto = set(lista)
print(conjunto)
input()
# Saida: {40, 10, 20, 30}
# Conjuntos não podem ter dois itens com o mesmo valor. Por isso que ao converter os valores repetidos são excluidos.
# E tambem não guarda nenhum ordem.

# Questão 03. Dada a lista numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], utilize a acesso em sublistas para obter: a) Os três primeiros elementos. b) Os elementos do índice 5 ao 8.
limpar_tela()
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# a)
print(numeros[:3])
# b)
print(numeros[5:9])
input()

# Questão 04. Dada a string texto = "banana", como você usaria um dicionário para contar quantas vezes cada letra aparece? (Ex: {'b': 1, 'a': 3, 'n': 2}).
limpar_tela()
texto = "banana"
dic = {}

for i in texto:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

print(dic)
input()

# Questão 05. Crie uma estrutura que represente uma lista de alunos, onde cada aluno é um dicionário contendo "nome" e uma lista de "notas". Como você acessaria a segunda nota do primeiro aluno?
limpar_tela()
alunos = [
    {
        "nome" : "Aluno1",
        "notas" : [1.0,2.0,3.0,4.0]
    },
    {
        "nome" : "Aluno1",
        "notas" : [1.1,2.2,3.3,4.4]
    }
]

print(alunos[0]["notas"][1])
input()

# Questão 06. A partir de uma lista de nomes ['ana', 'bia', 'caio'], crie um dicionário onde a chave é o nome e o valor é o número de letras desse nome.
limpar_tela()
nomes = ['ana', 'bia', 'caio']
dic = {}

for texto in nomes:
    for i in texto:
        if texto in dic:
            dic[texto] += 1
        else:
            dic[texto] = 1
print(dic)
input()
# Questão 07. Dada a lista de dicionários jogadores = [{'nome': 'A', 'pontos': 10}, {'nome': 'B', 'pontos': 50}, {'nome': 'C', 'pontos': 30}], como você ordenaria essa lista pela pontuação (do maior para o menor)?
limpar_tela()
jogadores = [{'nome': 'A', 'pontos': 10}, {'nome': 'B', 'pontos': 50}, {'nome': 'C', 'pontos': 30}]