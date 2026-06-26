"""
PlotaGrafico.py
===============
Lê os arquivos .res gerados pelo benchmark.py e plota os gráficos comparativos
(Array vs LinkedList) para cada operação de cada estrutura.

Os gráficos são salvos em: relatorio/graficos/<nome>.png

Uso
---
    python PlotaGrafico.py               # gera todos os gráficos
    python PlotaGrafico.py fila          # só fila
    python PlotaGrafico.py pilha         # só pilha
    python PlotaGrafico.py lista         # só lista

    # Modo legado (compatível com uso original):
    python PlotaGrafico.py "Título" arquivo1.res arquivo2.res ...
"""

import sys
import os
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


PASTA_RESULTADOS = "relatorio/resultados"
PASTA_GRAFICOS   = "relatorio/graficos"

# Cores fixas por backend
COR = {
    'Array':      '#2563EB',   # azul
    'LinkedList': '#DC2626',   # vermelho
}

# Anotações Big-O por operação
ANOTACOES = {
    'enqueue': "Array → O(1)  |  LinkedList → O(n)",
    'dequeue': "Array → O(n)  |  LinkedList → O(1)",
    'push':    "Ambos → O(1)  (constantes diferentes)",
    'pop':     "Ambos → O(1)  (constantes diferentes)",
    'add':     "Array → O(1)* |  LinkedList → O(n)",
    'get':     "Array → O(1)  |  LinkedList → O(n)",
    'insert':  "Array → O(n)  |  LinkedList → O(1)",
    'remove':  "Array → O(n)  |  LinkedList → O(1)",
}

# Grupos: cada entrada define um gráfico com suas duas séries
GRAFICOS = {
    'fila': [
        ("Fila – enqueue", "enqueue", "Fila-enqueue-Array", "Fila-enqueue-LinkedList"),
        ("Fila – dequeue", "dequeue", "Fila-dequeue-Array", "Fila-dequeue-LinkedList"),
    ],
    'pilha': [
        ("Pilha – push", "push", "Pilha-push-Array", "Pilha-push-LinkedList"),
        ("Pilha – pop",  "pop",  "Pilha-pop-Array",  "Pilha-pop-LinkedList"),
    ],
    'lista': [
        ("Lista – add",    "add",    "Lista-add-Array",    "Lista-add-LinkedList"),
        ("Lista – get",    "get",    "Lista-get-Array",    "Lista-get-LinkedList"),
        ("Lista – insert", "insert", "Lista-insert-Array", "Lista-insert-LinkedList"),
        ("Lista – remove", "remove", "Lista-remove-Array", "Lista-remove-LinkedList"),
    ],
}


# ═══════════════════════════════════════════════════════════════════════════ #
#  Leitura de .res                                                            #
# ═══════════════════════════════════════════════════════════════════════════ #

def ler_res(nome_arquivo: str) -> dict:
    """
    Lê um arquivo .res e retorna:
        { 'algoritmo': str, 'n': int, 'tempos': [float, ...] }
    """
    caminho = f"{PASTA_RESULTADOS}/{nome_arquivo}.res"
    if not os.path.exists(caminho):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}\n"
                                f"Execute benchmark.py primeiro.")
    with open(caminho) as f:
        cabecalho = f.readline().split(";")
        algoritmo = cabecalho[0].strip()
        n         = int(cabecalho[1].strip())
        tempos    = [float(linha) for linha in f if linha.strip()]
    return {'algoritmo': algoritmo, 'n': n, 'tempos': tempos}


# ═══════════════════════════════════════════════════════════════════════════ #
#  Plotagem                                                                   #
# ═══════════════════════════════════════════════════════════════════════════ #

def plotar(titulo: str, operacao: str, res_array: dict, res_ll: dict):
    """Gera e salva um gráfico comparativo Array vs LinkedList."""
    os.makedirs(PASTA_GRAFICOS, exist_ok=True)

    n      = res_array['n']
    passo  = n // len(res_array['tempos'])
    ns     = list(range(passo, n + 1, passo))

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(ns, res_array['tempos'], color=COR['Array'],
            linestyle='-',  marker='o', markersize=4, linewidth=2.5, label='Array')
    ax.plot(ns, res_ll['tempos'],   color=COR['LinkedList'],
            linestyle='--', marker='s', markersize=4, linewidth=2.5, label='LinkedList')

    ax.set_xlabel("Tamanho da entrada (n)", fontsize=14)
    ax.set_ylabel("Tempo médio (ms)",       fontsize=14)
    ax.set_title(titulo, fontsize=15, fontweight='bold')
    ax.legend(fontsize=12)
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.5f'))

    anotacao = ANOTACOES.get(operacao, "")
    if anotacao:
        ax.annotate(
            anotacao,
            xy=(0.97, 0.05), xycoords='axes fraction',
            ha='right', va='bottom', fontsize=11,
            bbox=dict(boxstyle='round,pad=0.3', fc='lightyellow', ec='gray', alpha=0.8),
        )

    nome_arquivo = f"{PASTA_GRAFICOS}/{titulo.replace(' ', '_').replace('–','').replace('  ',' ')}.png"
    plt.tight_layout()
    plt.savefig(nome_arquivo, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  ✔ Gráfico salvo: {nome_arquivo}")


# ═══════════════════════════════════════════════════════════════════════════ #
#  Modo automático (lê todos os .res do grupo)                                #
# ═══════════════════════════════════════════════════════════════════════════ #

def gerar_graficos(alvo: str):
    grupos = GRAFICOS if alvo == 'todos' else {alvo: GRAFICOS[alvo]}

    for grupo, entradas in grupos.items():
        print(f"\n📈 Gerando gráficos: {grupo.upper()}")
        for titulo, operacao, nome_arr, nome_ll in entradas:
            try:
                res_arr = ler_res(nome_arr)
                res_ll  = ler_res(nome_ll)
                plotar(titulo, operacao, res_arr, res_ll)
            except FileNotFoundError as e:
                print(f"  ⚠ {e}")


# ═══════════════════════════════════════════════════════════════════════════ #
#  Modo legado: python PlotaGrafico.py "Título" arq1.res arq2.res ...        #
# ═══════════════════════════════════════════════════════════════════════════ #

def modo_legado(titulo: str, arquivos: list):
    """Compatível com o uso original: plota N séries de arquivos .res."""
    os.makedirs(PASTA_GRAFICOS, exist_ok=True)

    series = []
    n_ref  = None

    for arq in arquivos:
        dados = ler_res(arq.replace('.res', '').replace(f"{PASTA_RESULTADOS}/", ""))
        if n_ref is None:
            n_ref = dados['n']
        elif n_ref != dados['n']:
            print("ERRO: arquivos com N diferentes. Rode o benchmark com o mesmo N_MAX.")
            return
        series.append(dados)

    passo = n_ref // len(series[0]['tempos'])
    ns    = list(range(passo, n_ref + 1, passo))

    fig, ax = plt.subplots(figsize=(10, 6))
    cores = list(COR.values()) + ['#16A34A', '#9333EA']
    for i, s in enumerate(series):
        ax.plot(ns, s['tempos'], linewidth=2.5, label=s['algoritmo'],
                color=cores[i % len(cores)])

    ax.set_xlabel("Tamanho da entrada (n)", fontsize=14)
    ax.set_ylabel("Tempo médio (ms)",       fontsize=14)
    ax.set_title(titulo, fontsize=15, fontweight='bold')
    ax.legend(fontsize=12)
    ax.grid(True, linestyle=':', alpha=0.6)

    nome_arquivo = f"{PASTA_GRAFICOS}/{titulo.replace(' ', '_')}.png"
    plt.tight_layout()
    plt.savefig(nome_arquivo, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✔ Gráfico salvo: {nome_arquivo}")


# ═══════════════════════════════════════════════════════════════════════════ #
#  Entrada principal                                                           #
# ═══════════════════════════════════════════════════════════════════════════ #

if __name__ == "__main__":
    args = sys.argv[1:]

    # Modo legado: primeiro arg é título, restantes são arquivos .res
    if len(args) >= 2 and args[1].endswith('.res'):
        modo_legado(args[0], args[1:])

    # Modo automático
    else:
        alvo = args[0].lower() if args else 'todos'
        opcoes = list(GRAFICOS.keys()) + ['todos']
        if alvo not in opcoes:
            print(f"Opção inválida. Use: {opcoes}")
        else:
            gerar_graficos(alvo)
            print(f"\n✅ Gráficos salvos em ./{PASTA_GRAFICOS}/")
