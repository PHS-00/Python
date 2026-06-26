"""
exemplos/historico_web.py
=========================
Exemplo de uso da PILHA: Histórico de navegação web.

- Visitar uma página  → push
- Voltar (back)       → pop  (retorna à página anterior)
- Ver página atual    → peek
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from modelos.pilha import Stack


class HistoricoWeb:
    """
    Simula o histórico de um navegador web usando Pilha.
    Cada aba mantém sua própria pilha de URLs visitadas.

    Complexidade:
        visitar()  → push  → Array O(1)*  | LinkedList O(1)
        voltar()   → pop   → Array O(1)   | LinkedList O(1)
        atual()    → peek  → Array O(1)   | LinkedList O(1)
    """

    def __init__(self, backend: str = 'array'):
        self._pilha  = Stack(backend=backend)
        self.backend = backend
        self.log: list[str] = []   # registro de ações para exibição

    # ── operações ────────────────────────────────────────────────────────── #

    def visitar(self, url: str) -> str:
        self._pilha.push(url)
        msg = f"Visitando → {url}"
        self.log.append(msg)
        return msg

    def voltar(self) -> str:
        if len(self._pilha) <= 1:
            msg = "Não há página anterior para voltar."
            self.log.append(msg)
            return msg
        saiu = self._pilha.pop()
        atual = self._pilha.peek()
        msg = f"Voltando de '{saiu}' → '{atual}'"
        self.log.append(msg)
        return msg

    def atual(self) -> str | None:
        return self._pilha.peek()

    def historico(self) -> list[str]:
        """Retorna o histórico do mais antigo ao mais recente."""
        return list(self._pilha._data)   # itera sobre Array.items ou LinkedList

    def limpar(self):
        self._pilha.clear()
        self.log.clear()

    def esta_vazio(self) -> bool:
        return self._pilha.is_empty()

    def tamanho(self) -> int:
        return len(self._pilha)
