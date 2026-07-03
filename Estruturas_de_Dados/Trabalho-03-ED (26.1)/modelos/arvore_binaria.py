class NodeBST:
    """Nó da Árvore Binária de Busca que guardará as colisões."""
    def __init__(self, chave, valor):
        self.chave = chave       # Será o CPF (inteiro)
        self.valor = valor       # Dicionário/Objeto com Nome, Sobrenome, Idade
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    """Implementação da BST para gerenciar os elementos colididos em um mesmo índice."""
    def __init__(self):
        self.raiz = None

    def inserir(self, chave, valor):
        if self.raiz is None:
            self.raiz = NodeBST(chave, valor)
            return
        
        atual = self.raiz
        while True:
            if chave == atual.chave:
                atual.valor = valor  # Atualiza se a chave já existir
                break
            elif chave < atual.chave:
                if atual.esquerda is None:
                    atual.esquerda = NodeBST(chave, valor)
                    break
                atual = atual.esquerda
            else:
                if atual.direita is None:
                    atual.direita = NodeBST(chave, valor)
                    break
                atual = atual.direita

    def buscar(self, chave):
        atual = self.raiz
        while atual is not None:
            if chave == atual.chave:
                return atual.valor
            elif chave < atual.chave:
                atual = atual.esquerda
            else:
                atual = atual.direita
        return None

    def remover(self, chave):
        self.raiz = self._remover_recursivo(self.raiz, chave)

    def _remover_recursivo(self, no, chave):
        if no is None:
            return None
        
        if chave < no.chave:
            no.esquerda = self._remover_recursivo(no.esquerda, chave)
        elif chave > no.chave:
            no.direita = self._remover_recursivo(no.direita, chave)
        else:
            # Caso 1 e 2: Nó com apenas um filho ou folha
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda
            
            # Caso 3: Nó com dois filhos
            sucessor = self._min_valor_no(no.direita)
            no.chave = sucessor.chave
            no.valor = sucessor.valor
            no.direita = self._remover_recursivo(no.direita, sucessor.chave)
            
        return no

    def _min_valor_no(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual