"""
benchmark.py
============
Executa os testes de desempenho (Big-O empírico) para Fila, Pilha e Lista,
comparando os backends Array e LinkedList em cada operação.

Os resultados são salvos em: relatorio/resultados/<nome>.res

Formato do .res
---------------
    <nome_da_serie>;<N_MAX>
    <tempo_ms_para_n=passo>
    <tempo_ms_para_n=2*passo>
    ...

Uso
---
    python benchmark.py          # roda todos
    python benchmark.py fila
    python benchmark.py pilha
    python benchmark.py lista
"""

import sys
import os
import time
import gc

from modelos.fila  import Queue
from modelos.pilha import Stack
from modelos.lista import List


# ═══════════════════════════════════════════════════════════════════════════ #
#  Configurações – altere aqui para mudar o tamanho dos testes               #
# ═══════════════════════════════════════════════════════════════════════════ #

N_MAX      = 3_000        # mesmo valor para TODOS os testes
PASSO      = 100          # incremento entre cada ponto medido
NS         = list(range(PASSO, N_MAX + 1, PASSO))   # [100, 200, ..., 3000]
REPETICOES = 5            # média de N execuções por ponto (reduz ruído)

PASTA_RESULTADOS = "relatorio/resultados"


# ═══════════════════════════════════════════════════════════════════════════ #
#  Motor de medição                                                           #
# ═══════════════════════════════════════════════════════════════════════════ #

def medir_ms(fn, *args) -> float:
    """Executa fn(*args) REPETICOES vezes e retorna a média em ms."""
    gc.disable()
    tempos = []
    for _ in range(REPETICOES):
        inicio = time.perf_counter()
        fn(*args)
        tempos.append(time.perf_counter() - inicio)
    gc.enable()
    return (sum(tempos) / len(tempos)) * 1000


def medir_serie(setup_fn, op_fn) -> list:
    """
    Para cada n em NS:
      1. Constrói a estrutura com setup_fn(n)
      2. Mede o tempo de op_fn(estrutura, n)
    Retorna lista de tempos em ms.
    """
    tempos = []
    for n in NS:
        estrutura = setup_fn(n)
        tempos.append(medir_ms(op_fn, estrutura, n))
    return tempos


# ═══════════════════════════════════════════════════════════════════════════ #
#  Persistência                                                               #
# ═══════════════════════════════════════════════════════════════════════════ #

def salvar_res(nome: str, tempos: list):
    """
    Salva em formato compatível com PlotaGrafico.py:
        <nome>;<N_MAX>
        <t1>
        <t2>
        ...
    """
    os.makedirs(PASTA_RESULTADOS, exist_ok=True)
    caminho = f"{PASTA_RESULTADOS}/{nome}.res"
    with open(caminho, "w") as f:
        f.write(f"{nome};{N_MAX}\n")
        for t in tempos:
            f.write(f"{t}\n")
    print(f"  ✔ Salvo: {caminho}")


# ═══════════════════════════════════════════════════════════════════════════ #
#  Benchmarks – FILA                                                          #
# ═══════════════════════════════════════════════════════════════════════════ #

def benchmark_fila():
    print("\n📊 Benchmark: FILA")

    def setup(backend, n):
        q = Queue(backend=backend)
        for i in range(n - 1):
            q.enqueue(i)
        return q

    print("  -> enqueue")
    salvar_res("Fila-enqueue-Array",      medir_serie(lambda n: setup('array', n),      lambda q, n: q.enqueue(n)))
    salvar_res("Fila-enqueue-LinkedList", medir_serie(lambda n: setup('linkedlist', n), lambda q, n: q.enqueue(n)))

    print("  -> dequeue")
    salvar_res("Fila-dequeue-Array",      medir_serie(lambda n: setup('array', n),      lambda q, n: q.dequeue()))
    salvar_res("Fila-dequeue-LinkedList", medir_serie(lambda n: setup('linkedlist', n), lambda q, n: q.dequeue()))


# ═══════════════════════════════════════════════════════════════════════════ #
#  Benchmarks – PILHA                                                         #
# ═══════════════════════════════════════════════════════════════════════════ #

def benchmark_pilha():
    print("\n📊 Benchmark: PILHA")

    def setup(backend, n):
        s = Stack(backend=backend)
        for i in range(n - 1):
            s.push(i)
        return s

    print("  -> push")
    salvar_res("Pilha-push-Array",      medir_serie(lambda n: setup('array', n),      lambda s, n: s.push(n)))
    salvar_res("Pilha-push-LinkedList", medir_serie(lambda n: setup('linkedlist', n), lambda s, n: s.push(n)))

    print("  -> pop")
    salvar_res("Pilha-pop-Array",      medir_serie(lambda n: setup('array', n),      lambda s, n: s.pop()))
    salvar_res("Pilha-pop-LinkedList", medir_serie(lambda n: setup('linkedlist', n), lambda s, n: s.pop()))


# ═══════════════════════════════════════════════════════════════════════════ #
#  Benchmarks – LISTA                                                         #
# ═══════════════════════════════════════════════════════════════════════════ #

def benchmark_lista():
    print("\n📊 Benchmark: LISTA")

    def setup(backend, n):
        lst = List(backend=backend)
        for i in range(n - 1):
            lst.add(i)
        return lst

    print("  -> add")
    salvar_res("Lista-add-Array",      medir_serie(lambda n: setup('array', n),      lambda lst, n: lst.add(n)))
    salvar_res("Lista-add-LinkedList", medir_serie(lambda n: setup('linkedlist', n), lambda lst, n: lst.add(n)))

    print("  -> get (indice do meio)")
    salvar_res("Lista-get-Array",      medir_serie(lambda n: setup('array', n),      lambda lst, n: lst.get(len(lst) // 2)))
    salvar_res("Lista-get-LinkedList", medir_serie(lambda n: setup('linkedlist', n), lambda lst, n: lst.get(len(lst) // 2)))

    print("  -> insert (indice 0)")
    salvar_res("Lista-insert-Array",      medir_serie(lambda n: setup('array', n),      lambda lst, n: lst.insert(0, -1)))
    salvar_res("Lista-insert-LinkedList", medir_serie(lambda n: setup('linkedlist', n), lambda lst, n: lst.insert(0, -1)))

    print("  -> remove (primeiro)")
    salvar_res("Lista-remove-Array",      medir_serie(lambda n: setup('array', n),      lambda lst, n: lst.remove(lst.get(0))))
    salvar_res("Lista-remove-LinkedList", medir_serie(lambda n: setup('linkedlist', n), lambda lst, n: lst.remove(lst._data.head.data)))


# ═══════════════════════════════════════════════════════════════════════════ #
#  Entrada principal                                                           #
# ═══════════════════════════════════════════════════════════════════════════ #

BENCHMARKS = {
    'fila':  benchmark_fila,
    'pilha': benchmark_pilha,
    'lista': benchmark_lista,
}

if __name__ == "__main__":
    alvo = sys.argv[1].lower() if len(sys.argv) > 1 else 'todos'

    if alvo == 'todos':
        for fn in BENCHMARKS.values():
            fn()
    elif alvo in BENCHMARKS:
        BENCHMARKS[alvo]()
    else:
        print(f"Opcao invalida. Use: {list(BENCHMARKS.keys())} ou omita para rodar tudo.")

    print(f"\nResultados salvos em ./{PASTA_RESULTADOS}/")
