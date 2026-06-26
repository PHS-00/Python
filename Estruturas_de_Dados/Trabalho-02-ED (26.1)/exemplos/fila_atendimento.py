"""
exemplos/fila_atendimento.py
============================
Exemplo de uso da FILA: Sistema de atendimento (call center / suporte).

- Cliente chega       → enqueue
- Atender próximo     → dequeue
- Ver próximo da fila → peek
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from modelos.fila import Queue


class FilaAtendimento:
    """
    Simula uma fila de atendimento ao cliente (FIFO).

    Complexidade:
        chegada()   → enqueue → Array O(1)*  | LinkedList O(n)
        atender()   → dequeue → Array O(n)   | LinkedList O(1)
        proximo()   → peek    → Array O(1)   | LinkedList O(1)
    """

    def __init__(self, backend: str = 'array'):
        self._fila      = Queue(backend=backend)
        self.backend    = backend
        self.atendidos  = 0
        self.log: list[str] = []

    # ── operações ────────────────────────────────────────────────────────── #

    def chegada(self, nome: str) -> str:
        self._fila.enqueue(nome)
        posicao = len(self._fila)
        msg = f"{nome} entrou na fila. (posição {posicao})"
        self.log.append(msg)
        return msg

    def atender(self) -> str:
        if self._fila.is_empty():
            msg = "Fila vazia — nenhum cliente para atender."
            self.log.append(msg)
            return msg
        cliente = self._fila.dequeue()
        self.atendidos += 1
        proximo = self._fila.peek()
        msg = f"Atendendo: {cliente}"
        if proximo:
            msg += f" | Próximo: {proximo}"
        self.log.append(msg)
        return msg

    def proximo(self) -> str | None:
        return self._fila.peek()

    def fila_atual(self) -> list[str]:
        """Retorna a lista de clientes em ordem de chegada."""
        if self.backend == 'array':
            return list(self._fila._data.items)
        else:
            return list(self._fila._data)

    def limpar(self):
        self._fila.clear()
        self.atendidos = 0
        self.log.clear()

    def esta_vazia(self) -> bool:
        return self._fila.is_empty()

    def tamanho(self) -> int:
        return len(self._fila)
