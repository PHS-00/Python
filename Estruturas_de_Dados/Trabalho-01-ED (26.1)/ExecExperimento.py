"""
Codigo para análise empirica matemática dos algoritmos iterativos e recursivos:
fibonacci, bubbleSort, MergeSort e QuickSort
"""
import time
import random
import os
import Fibonacci as fib
import Fatorial as fat
import OrdenacaoN2 as ordN2
import OrdenacaoNLog as ordNLog

def medirTempo(funcao, entrada):
    inicio = time.perf_counter()
    funcao(entrada)
    fim = time.perf_counter()
    return (fim - inicio)*1000
    
def salvaResultado(algoritmo,n, resultado, ordem = None):
    os.makedirs('resultados',exist_ok=True)
    if ordem != None:
        caminhoArquivo = os.path.join('resultados',f'{algoritmo}-{ordem}.res')
    else:
        caminhoArquivo = os.path.join('resultados',f'{algoritmo}.res')
    with open(caminhoArquivo,'w') as arquivo:
       if ordem != None:
        arquivo.write(f'{algoritmo}-{ordem};{n}\n')
       else:
        arquivo.write(f'{algoritmo};{n}\n')
       for item in resultado:
           arquivo.write(str(item)+"\n")
       arquivo.flush()
       arquivo.close()

def executaExperimento(algoritmo,numeros,funcao): 
    resultado = []
    for n in numeros:
        if(n%5==0):
            print(f'Executando {algoritmo} para entrada: {n}')
        resultado.append(medirTempo(funcao, n))
    salvaResultado(algoritmo,n+1,resultado)
    print(f'Finalizado experimento para {algoritmo} para entrada: {n+1}')

def executaExperimentoOrdenacao(algoritmo,numeros,funcao,ordem): 
    resultado = []
    n = len(numeros)
    for i in (range(1,len(numeros)+1)):
        if(n <= 100):
            if(i%10==0):
                print(f'Executando {algoritmo} para entrada: {i}')
        elif(n >= 100 and n <= 1000):
            if(i%100==0):
                print(f'Executando {algoritmo} para entrada: {i}')
        else:
            if(i%100==0):
                print(f'Executando {algoritmo} para entrada: {i}')
        resultado.append(medirTempo(funcao, numeros[:i+1]))
    salvaResultado(algoritmo,n,resultado,ordem)
    print(f'Finalizado experimento para {algoritmo} para entrada: {n}')

   
if __name__ == "__main__":
    algoritmos = ["Fatorial-Iterativo","Fatorial-Recursivo",
                  "Fibonacci-Iterativo","Fibonacci-Recursivo",
                  "OrdenacaoN2-Iterativo","OrdenacaoN2-Recursivo",
                  "OrdenacaoNLog-Iterativo", "OrdenacaoNLog-Recursivo"]
    funcoes = [               
               fat.fatorialIt,fat.fatorial,
               fib.fibonacciIt,fib.fibonacci,
               ordN2.ordenarIterativoN2,ordN2.ordenarRecursivoN2,
               ordNLog.ordenarIterativoNLog,ordNLog.ordenarRecursivoNLog]
    for i in range(0,len(algoritmos)):
        print(f'[{i+1}] -> {algoritmos[i]}')
    opcao = int(input('Escolha qual algoritmo quer executar ou [0] para finalizar: '))
    if opcao > 0 and opcao <= len(funcoes):
        n = int(input('Informe o valor da máximo da entrada n: '))
        if opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4:
            numeros = range(0,n)
            print("Isso pode levar um tempo ... ")         
            executaExperimento(algoritmos[opcao-1],numeros,funcoes[opcao-1])        
        else:
            ordem = int(input('Gerar lista ? 0-Não Ordenada, 1-Ordenada, 2-Inversamente Ordenada: '))
            legenda = ["Nao-Ordenada", "Ordenada", "Inversamente-Ordenada"]
            if ordem == 0:
                numeros = list(range(0,n))
                random.shuffle(numeros)
            elif ordem == 1:
                numeros = list(range(0,n))
            else:
                numeros = list(range(n,0,-1)) 
            print("Isso pode levar um tempo ... ")
            executaExperimentoOrdenacao(algoritmos[opcao-1],numeros,funcoes[opcao-1],legenda[ordem])
