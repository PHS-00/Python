from modelos.array import Array
from modelos.lista_ligada import LinkedList


class Stack:
    """
    Pilha (Stack) com suporte a dois backends:
      - 'array'    : usa lista Python            → push O(1) amortizado, pop O(1)
      - 'linkedlist': usa lista ligada (prepend) → push O(1),            pop O(1)

    Ambos os backends são O(1) para push/pop; o benchmark mostrará as
    constantes ocultas de cada implementação.

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
        return f"Stack[{self.backend}]: {self._data}"

    def clear(self):
        self._data.clear()

    # ------------------------------------------------------------------ #
    #  Operações da pilha                                                  #
    # ------------------------------------------------------------------ #

    def push(self, item):
        """
        Empilha um item no topo.
        Array     → O(1) amortizado (append no final da lista Python)
        LinkedList → O(1) (prepend: novo nó aponta para head)
        """
        if self.backend == 'array':
            self._data.items.append(item)
        else:
            self._data.prepend(item)   # topo = head

    def pop(self):
        """
        Desempilha o item do topo.
        Array     → O(1) (pop do final)
        LinkedList → O(1) (remove_first retira o head)
        """
        if self.is_empty():
            raise IndexError("Pilha vazia")
        if self.backend == 'array':
            return self._data.items.pop()
        else:
            return self._data.remove_first()

    def peek(self):
        """Retorna o topo sem remover."""
        if self.is_empty():
            return None
        if self.backend == 'array':
            return self._data.items[-1]
        else:
            return self._data.head.data
