from modelos.array import Array
from modelos.lista_ligada import LinkedList


class List:
    """
    Lista (List) com suporte a dois backends:
      - 'array'    : usa lista Python
      - 'linkedlist': usa lista ligada

    Complexidades comparadas
    ------------------------
    Operação        Array       LinkedList
    add (fim)       O(1)*       O(n)
    insert (meio)   O(n)        O(n)
    remove          O(n)        O(n)
    get (índice)    O(1)        O(n)   ← diferença crítica

    *amortizado

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
        return f"List[{self.backend}]: {self._data}"

    def clear(self):
        self._data.clear()

    # ------------------------------------------------------------------ #
    #  Operações da lista                                                  #
    # ------------------------------------------------------------------ #

    def add(self, item):
        """
        Adiciona ao final.
        Array     → O(1) amortizado
        LinkedList → O(n) (percorre até o fim)
        """
        if self.backend == 'array':
            self._data.items.append(item)
        else:
            self._data.append(item)

    def insert(self, index: int, item):
        """
        Insere em posição arbitrária.
        Array     → O(n) (deslocamento dos elementos à direita)
        LinkedList → O(n) (percorre até o índice)
        """
        if self.backend == 'array':
            self._data.items.insert(index, item)
        else:
            self._data.insert_at(index, item)

    def remove(self, item):
        """
        Remove a primeira ocorrência do item.
        Array     → O(n)
        LinkedList → O(n)
        """
        if self.backend == 'array':
            self._data.items.remove(item)
        else:
            self._data.remove(item)

    def get(self, index: int):
        """
        Acesso por índice.
        Array     → O(1) (acesso direto à memória)
        LinkedList → O(n) (percorre nó a nó)
        """
        if self.backend == 'array':
            return self._data.items[index]
        else:
            return self._data.get(index)
