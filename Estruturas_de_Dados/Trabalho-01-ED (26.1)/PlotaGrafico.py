import matplotlib.pyplot as plt
import sys

'''
Módulo para plotar gráfico conforme arquivos de resultados
autor: Arthur Souza
'''

def gerarGrafico(titulo, algoritmos, numeros, resultados):
    ''' 
    Gera um gráfico com o título e para os algoritmos, numeros e resultados
    obtidos dos arquivos com resultados
    '''
    plt.figure(figsize=(10,6))
    #print(resultados)
    for i in range(0,len(algoritmos)):
        plt.plot(numeros, resultados[i], linewidth=4, label=algoritmos[i])        
    plt.xlabel("Tamanho da entrada (n)",fontsize=18)
    plt.ylabel("Tempo de execução (ms)",fontsize=18)
    plt.title(titulo,fontsize=18)
    plt.legend()
    plt.grid(True)
    plt.show()

def lendoResultados(arquivo):
    '''
    Função para ler os resultados do arquivo.
    Recebe o caminho de para um [arquivo]
    Retorna um dicionário com os dados dos resultados
    algoritmo - nome do algoritmo
    n - quantidade da entrada
    resultados - dados de tempo de execução
    '''
    dados = {}
    resultados = list()
    with open(arquivo) as fil:
       linha1 = fil.readline().split(";")
       dados["algoritmo"] = linha1[0]
       dados["n"] = linha1[1]
       for linha in fil:
           resultados.append(float(linha))
       fil.close()
    dados["resultados"] = resultados
    return dados
    

if __name__ == "__main__":
    '''
    Lê os parametros de arquivos e gera o gráfico
    Exemplo de uso:
    python PlotaGrafico.py Fibonacci ./resultados/Fibonacci-Iterativo.res ./resultados/Fibonacci-Recursivo.res
    '''
    if len(sys.argv) > 2:
        titulo = sys.argv[1]
        algoritmos = []
        resultados = []
        n = 0
        entradasDiferentes = False
        for i in range(2,len(sys.argv)):
            dados = lendoResultados(sys.argv[i])
            algoritmos.append(dados["algoritmo"])
            resultados.append(dados["resultados"])
            nTemp = int(dados["n"])
            if (n == 0): 
                n = nTemp
            elif n != nTemp:
                entradasDiferentes = True
            else:
                next;
        if(not entradasDiferentes):
            gerarGrafico(titulo,algoritmos,list(range(0,n)),resultados)
        else:
            print("A quantidade das entradas dos arquivos é diferente.\nRepita o experimento para cada algoritmo com o mesmo número de entrada")

    else:
        print("Informe os parametros no formato: python PlotaGrafico.py [Título do Gráfico] [Arquivo] [Arquivo] ...")