class HashTable():
    def __init__(self, capacidade=100):
        self.tabela = [None] * capacidade

    def hash(self, chave):
        return chave % len(self.tabela)

    def adicionar(self, chave, valor):
        indice = self.hash(chave)
        self.tabela[indice] = valor

    def buscar(self, chave):
        indice = self.hash(chave)
        return self.tabela[indice]

    def remover(self, chave):
        indice = self.hash(chave)
        self.tabela[indice] = None

    def atualizar(self, chave, valor):
        indice = self.hash(chave)
        self.tabela[indice] = valor