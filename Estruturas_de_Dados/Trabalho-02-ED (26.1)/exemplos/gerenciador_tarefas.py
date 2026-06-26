"""
exemplos/gerenciador_tarefas.py
================================
Exemplo de uso da LISTA: Gerenciador de tarefas (To-Do List).

- Adicionar tarefa ao final     → add
- Inserir tarefa com prioridade → insert(0, tarefa)  ← topo da lista
- Concluir / remover tarefa     → remove
- Acessar tarefa por índice     → get
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from modelos.lista import List


class GerenciadorTarefas:
    """
    Lista de tarefas com suporte a prioridade (inserção no início).

    Complexidade:
        adicionar()  → add        → Array O(1)*  | LinkedList O(n)
        prioritaria()→ insert(0)  → Array O(n)   | LinkedList O(1)
        concluir()   → remove     → Array O(n)   | LinkedList O(n)
        buscar()     → get(index) → Array O(1)   | LinkedList O(n)
    """

    def __init__(self, backend: str = 'array'):
        self._lista  = List(backend=backend)
        self.backend = backend
        self.concluidas: list[str] = []
        self.log: list[str] = []

    # ── operações ────────────────────────────────────────────────────────── #

    def adicionar(self, tarefa: str) -> str:
        self._lista.add(tarefa)
        msg = f"Tarefa adicionada: '{tarefa}' (posição {len(self._lista)})"
        self.log.append(msg)
        return msg

    def prioritaria(self, tarefa: str) -> str:
        self._lista.insert(0, tarefa)
        msg = f"Tarefa prioritária: '{tarefa}' → inserida no topo"
        self.log.append(msg)
        return msg

    def concluir(self, tarefa: str) -> str:
        try:
            self._lista.remove(tarefa)
            self.concluidas.append(tarefa)
            msg = f"Tarefa concluída: '{tarefa}'"
        except (ValueError, IndexError):
            msg = f"Tarefa '{tarefa}' não encontrada."
        self.log.append(msg)
        return msg

    def buscar(self, indice: int) -> str:
        try:
            return self._lista.get(indice)
        except IndexError:
            return None

    def tarefas(self) -> list[str]:
        """Retorna todas as tarefas pendentes em ordem."""
        if self.backend == 'array':
            return list(self._lista._data.items)
        else:
            return list(self._lista._data)

    def limpar(self):
        self._lista.clear()
        self.concluidas.clear()
        self.log.clear()

    def esta_vazia(self) -> bool:
        return self._lista.is_empty()

    def tamanho(self) -> int:
        return len(self._lista)
