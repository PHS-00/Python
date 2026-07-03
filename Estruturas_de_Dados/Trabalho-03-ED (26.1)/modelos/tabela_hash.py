# class HashTable():
#     def __init__(self, capacidade=100):
#         self.tabela = [None] * capacidade

#     def hash(self, chave):
#         return chave % len(self.tabela)

#     def adicionar(self, chave, valor):
#         indice = self.hash(chave)
#         self.tabela[indice] = valor

#     def buscar(self, chave):
#         indice = self.hash(chave)
#         return self.tabela[indice]

#     def remover(self, chave):
#         indice = self.hash(chave)
#         self.tabela[indice] = None

#     def atualizar(self, chave, valor):
#         indice = self.hash(chave)
#         self.tabela[indice] = valor

# Marcador de "lápide": indica um slot que já teve uma chave, mas foi removida.
# É diferente de None (slot nunca usado) porque, numa sondagem linear, não
# podemos parar a busca num slot removido -- a chave procurada pode estar
# um pouco mais à frente, empurrada pela colisão original.
_REMOVIDO = object()


class HashTable():
    def __init__(self, capacidade=100):
        self.capacidade = capacidade
        self.chaves = [None] * capacidade   # guarda a CHAVE de cada slot (para achar/comparar depois)
        self.tabela = [None] * capacidade   # guarda o VALOR de cada slot

    def hash(self, chave):
        return chave % self.capacidade

    def _localizar_slot(self, chave):
        """Sondagem linear: percorre slot a slot a partir de hash(chave) até
        achar a própria chave, um slot vazio (None) ou dar a volta na tabela.

        Retorna (indice, encontrado):
          - encontrado=True  -> indice é o slot onde a chave está
          - encontrado=False -> indice é o primeiro slot livre/lápide para inserir
                                 (ou None se a tabela estiver cheia)
        """
        indice_inicial = self.hash(chave)
        primeiro_livre = None

        for tentativa in range(self.capacidade):
            pos = (indice_inicial + tentativa) % self.capacidade

            if self.chaves[pos] is None:
                # slot nunca usado -> a chave definitivamente não está na tabela
                return (primeiro_livre if primeiro_livre is not None else pos), False

            if self.chaves[pos] is _REMOVIDO:
                # slot livre para reaproveitar numa inserção, mas a busca continua
                if primeiro_livre is None:
                    primeiro_livre = pos
                continue

            if self.chaves[pos] == chave:
                return pos, True

        # Deu a volta inteira na tabela sem achar vazio nem a chave -> tabela cheia
        return primeiro_livre, False

    def adicionar(self, chave, valor):
        pos, encontrado = self._localizar_slot(chave)
        if pos is None:
            raise Exception("Tabela hash cheia - aumente a capacidade")
        self.chaves[pos] = chave
        self.tabela[pos] = valor

    def buscar(self, chave):
        pos, encontrado = self._localizar_slot(chave)
        return self.tabela[pos] if encontrado else None

    def remover(self, chave):
        pos, encontrado = self._localizar_slot(chave)
        if encontrado:
            self.chaves[pos] = _REMOVIDO
            self.tabela[pos] = None

    def atualizar(self, chave, valor):
        self.adicionar(chave, valor)  # adicionar já atualiza se a chave já existir