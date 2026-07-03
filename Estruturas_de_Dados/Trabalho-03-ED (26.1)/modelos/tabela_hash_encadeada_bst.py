from modelos.tabela_hash import HashTable
from modelos.arvore_binaria import ArvoreBinaria

class HashTableEncadeadaBST(HashTable):
    def __init__(self, capacidade=2003):
        # super() aciona o construtor da HashTable padrão com a nova capacidade
        super().__init__(capacidade)
    
    def _tratar_chave(self, chave):
        """Garante que o CPF em string vire inteiro para a função hash."""
        if isinstance(chave, str):
            return int(''.join(filter(str.isdigit, chave)))
        return chave

    # Sobrescrevemos o adicionar original para lidar com a Árvore
    def adicionar(self, chave, valor):
        chave_tratada = self._tratar_chave(chave)
        
        # REAPROVEITAMENTO: usa o método hash() que você já programou na classe pai!
        indice = self.hash(chave_tratada) 
        
        # Se o balde estiver vazio, colocamos a Árvore ali
        if self.tabela[indice] is None:
            self.tabela[indice] = ArvoreBinaria()
        
        # Delega a inserção para a árvore daquela posição
        self.tabela[indice].inserir(chave_tratada, valor)

    # Sobrescrevemos o buscar para procurar dentro da BST daquela posição
    def buscar(self, chave):
        chave_tratada = self._tratar_chave(chave)
        indice = self.hash(chave_tratada)
        
        if self.tabela[indice] is None:
            return None
        return self.tabela[indice].buscar(chave_tratada)

    # Sobrescrevemos o remover para retirar da BST daquela posição
    def remover(self, chave):
        chave_tratada = self._tratar_chave(chave)
        indice = self.hash(chave_tratada)
        
        if self.tabela[indice] is not None:
            self.tabela[indice].remover(chave_tratada)
            if self.tabela[indice].raiz is None:
                self.tabela[indice] = None