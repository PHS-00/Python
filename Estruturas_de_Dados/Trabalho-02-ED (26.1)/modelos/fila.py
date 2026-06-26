from modelos.array import Array
from modelos.lista_ligada import LinkedList


class Queue:
    """
    Fila (Queue) com suporte a dois backends:
      - 'array'    : usa lista Python internamente  → enqueue O(1), dequeue O(n)
      - 'linkedlist': usa lista ligada              → enqueue O(n)*, dequeue O(1)
                      (*O(1) se usarmos prepend + remove_first)

    Parâmetro
    ---------
    backend : str
        'array' (padrão) ou 'linkedlist'
    """

    BACKENDS = ('array', 'linkedlist')

    def __init__(self, backend: str = 'array'):
        if backend not in self.BACKENDS:
            raise ValueError(f"backend deve ser um de {self.BACKENDS}")
        self.backend = backend
        if backend == 'array':
            self._data = Array()
        else:
            self._data = LinkedList()

    # ------------------------------------------------------------------ #
    #  Interface comum                                                     #
    # ------------------------------------------------------------------ #

    def is_empty(self) -> bool:
        return self._data.is_empty()

    def __len__(self) -> int:
        return len(self._data)

    def __str__(self) -> str:
        return f"Queue[{self.backend}]: {self._data}"

    def clear(self):
        self._data.clear()

    # ------------------------------------------------------------------ #
    #  Operações da fila                                                   #
    # ------------------------------------------------------------------ #

    def enqueue(self, item):
        """
        Insere no final da fila.
        Array     → O(1) amortizado
        LinkedList → O(n)  (percorre até o fim para append)
        """
        if self.backend == 'array':
            self._data.items.append(item)
        else:
            self._data.append(item)   # LinkedList.append → O(n)

    def dequeue(self):
        """
        Remove do início da fila.
        Array     → O(n)  (items.pop(0) desloca todos os elementos)
        LinkedList → O(1) (remove_first apenas avança head)
        """
        if self.is_empty():
            raise IndexError("Fila vazia")
        if self.backend == 'array':
            return self._data.items.pop(0)
        else:
            return self._data.remove_first()

    def peek(self):
        """Retorna o primeiro elemento sem remover."""
        if self.is_empty():
            return None
        if self.backend == 'array':
            return self._data.items[0]
        else:
            return self._data.head.data
