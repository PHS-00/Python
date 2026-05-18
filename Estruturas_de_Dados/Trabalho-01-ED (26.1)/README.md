## Trabalho Complementar da Unidade I ##
Trabalho Complementar da Unidade I para compor a média final da unidade.
Esse trabalho busca auxiliar o estudo da análise experimental de algoritmos.
Os algoritmos utilizados:
 - Fibonacci
 - Fatorial
 - Ordenação N²
 - Ordenação Log(n)

## Requisitos do Ambiente ##
Para executar o experimento é necessário possuir instalado:
 - python >= 3.9 [Python] (https://www.python.org/downloads/)
 - Módulo [MathPlotLib](https://matplotlib.org/stable/install/index.html)

A execução do Algoritmo está centralizada pelo arquivo [ExecExperimento.py](./ExecExperimento.py)

### Executando no Terminal ###
Para executar o experimento abra um terminal de comando.
Acesse a pasta com o código do projeto e execute: 
```
python3.9 ExecExperimento.py
```
### Executando no VSCode ####
Abra a pasta do projeto no VSCode e execute o arquivo ExecExperimento.py

### Exemplo de Execução ###
O Experimento realiza a execução sequencial de várias listas com entradas variando de 0 até *[n]* para o algoritmo selecinado. Por exemplo, para executar o Fatorial-Iterativo:
```
python ExecExperimento.py
[1] -> Fatorial-Iterativo
[2] -> Fatorial-Recursivo
[3] -> Fibonacci-Iterativo
[4] -> Fibonacci-Recursivo
[5] -> OrdenacaoN2-Iterativo
[6] -> OrdenacaoN2-Recursivo
[7] -> OrdenacaoNLog-Iterativo
[8] -> OrdenacaoNLog-Recursivo
Escolha qual algoritmo quer executar ou [0] para finalizar: 1
Informe o valor da máximo da entrada n: 10
Executando Fatorial-Iterativo para entrada: 0
Executando Fatorial-Iterativo para entrada: 5
Finalizado experimento para Fatorial-Iterativo para entrada: 10
```

Ao executar o Fatorial-Iterativo para uma entrada n=10, o experimento irá executar o algoritmo 11 vezes, a primeira com n=0, a segunda com n=1, a terceira com n=2 e assim sucessivamente ate n=10.
Os tempos de execução para cada entrada são salvos em arquivos texto com extensão .res na pasta resultados.
Esses arquivos serão usados na plotagem do gráfico.  

__ALERTA__: Para um n=10.000, o experimento irá executar o algoritmo 10.0001 vezes variando o n de 0 a 10.000, assim irá levar um bom tempo para terminar. 


### Como executar o experimento ###
Inicie o experimento determinando o valor máximo da entrada que seu computador suportará para:
 - Fibonacci-Recursivo: teste os valores [10,20,30,40].
 - Ordenação N² Recursivo: teste [5000,7000,9000,10000]
Caso seja retornado algum erro de max recurssion depth, assuma o valor anterior como o limite máximo da sua máquina.

Se não for retornado erro, execute até os limites de 40 (Fibonacci) e 10000 (Ordenação)

# Experimento Fatorial e Fibonacci #
Execute o Script ExecExperimento.py para a entrada máxima dos algoritmos:
 - Fatorial-Iterativo
 - Fatorial-Recursivo.
 - Fibonacci-Iterativo
 - Fibonacci-Recursivo.

# Experimento Ordenação #
Execute o Script ExecExperimento.py para a entrada máxima dos algoritmos de Ordenação:
 - OrdenacaoN2-Iterativo
 - OrdenacaoN2-Recursivo
 - OrdenacaoNLog-Iterativo
 - OrdenacaoNLog-Recursivo
 
 __Teste__: Todas as opções de listas [ordenada, lista desordenada, lista não-ordenada], cada uma irá criar um arquivo em resultados.

# Plotando no Gráfico #
Execute o Script PlotaGrafico.py no Terminal.
Ele recebe parâmetros [titulo do gráfico] [arquivo01] [arquivo02] ...
A quantidade de arquivos pode variar permitindo gerar gráficos de vários resultados
Exemplo:
 -  python3.12 PlotaGrafico.py "Fibonnaci vs Fatorial" resultados/Fibonacci-Iterativo.res resultados/Fibonacci-Recursivo.res resultados/Fatorial-Iterativo.res resultados/Fatorial-Recursivo.res 
```
 python3.12 PlotaGrafico.py "Fibonnaci vs Fatorial" resultados/Fibonacci-Iterativo.res resultados/Fibonacci-Recursivo.res resultados/Fatorial-Iterativo.res resultados/Fatorial-Recursivo.res 
```