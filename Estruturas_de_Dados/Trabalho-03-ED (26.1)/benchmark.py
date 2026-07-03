import csv
import time
import os

# Importando as estruturas de dados
from modelos.tabela_hash import HashTable
from modelos.tabela_hash_encadeada_bst import HashTableEncadeadaBST

# ===================================================================
#            Seção de caregamento de dados de arquivos .csv
# ===================================================================
def carregar_dados_insercao(arquivo_nome):
    """Carrega os dados do arquivo de inserção (CPF, Nome, Sobrenome, Idade)."""
    dados = []
    with open(arquivo_nome, mode='r', encoding='utf-8') as f:
        leitor = csv.reader(f)
        for linha in leitor:
            if not linha:
                continue
            cpf, nome, sobrenome, idade = linha
            dados.append({
                'cpf': int(cpf),
                'valor': {'nome': nome, 'sobrenome': sobrenome, 'idade': int(idade)}
            })
    return dados

def carregar_dados_busca_remocao(arquivo_nome):
    """Carrega apenas os CPFs dos arquivos de busca ou remoção."""
    cpfs = []
    with open(arquivo_nome, mode='r', encoding='utf-8') as f:
        leitor = csv.reader(f)
        for linha in leitor:
            if not linha:
                continue
            cpfs.append(int(linha[0]))
    return cpfs


# ===================================================================
#          Seção de salvamento de dados do beachmark em .res
# ===================================================================
def salvar_arquivo_res(nome_estrutura, nome_operacao, tempos_individuais):
    """Gera o arquivo .res no formato solicitado."""
    nome_arquivo = f"./relatorio/resultados/{nome_estrutura}_{nome_operacao}.res"
    quantidade_testes = len(tempos_individuais)
    
    with open(nome_arquivo, mode='w', encoding='utf-8') as f:
        # Primeira linha: nome_da_estrutura_operacao;quantidade_total
        f.write(f"{nome_estrutura}_{nome_operacao};{quantidade_testes}\n")
        # Linhas seguintes: tempo um por um
        for tempo in tempos_individuais:
            f.write(f"{tempo:.18f}\n") # .18f garante alta precisão das casas decimais
            
    print(f"  -> Arquivo gerado com sucesso: {nome_arquivo}")


# ===================================================================
#                      Seção de teste de tempo
# ===================================================================
def rodar_benchmark():
    print("------------ Carregando arquivos CSV ------------")
    dados_insercao = carregar_dados_insercao('dados/insercao.csv')
    cpfs_busca = carregar_dados_busca_remocao('dados/busca.csv')
    cpfs_remocao = carregar_dados_busca_remocao('dados/remocao.csv')
    
    print(f"Total de inserções: {len(dados_insercao)}")
    print(f"Total de buscas: {len(cpfs_busca)}")
    print(f"Total de remoções: {len(cpfs_remocao)}")
    print("-" * 49)
    
    # Instanciando as duas estruturas
    tabela_linear = HashTable(capacidade=10003)
    tabela_bst = HashTableEncadeadaBST(capacidade=2003) # Capacidade padrão do seu arquivo original

    # Mapeamento para automação do benchmark
    estruturas = {
        "tabela_hash_linear": tabela_linear,
        "tabela_hash_arvore_binaria": tabela_bst
    }

    for nome_est, estrutura in estruturas.items():
        print(f"\n⏳ Iniciando execução para: {nome_est}")

        # --- 1. BENCHMARK DE INSERÇÃO (adicionar) ---
        tempos_insercao = []
        for item in dados_insercao:
            inicio = time.perf_counter()
            try:
                estrutura.adicionar(item['cpf'], item['valor'])
            except Exception as e:
                print(f"Erro ao adicionar na {nome_est}: {e}")
                break
            fim = time.perf_counter()
            tempos_insercao.append(fim - inicio)
        
        salvar_arquivo_res(nome_est, "adicionar", tempos_insercao)

        # --- 2. BENCHMARK DE BUSCA (buscar) ---
        tempos_busca = []
        for cpf in cpfs_busca:
            inicio = time.perf_counter()
            estrutura.buscar(cpf)
            fim = time.perf_counter()
            tempos_busca.append(fim - inicio)
            
        salvar_arquivo_res(nome_est, "buscar", tempos_busca)

        # --- 3. BENCHMARK DE REMOÇÃO (remover) ---
        tempos_remoçao = []
        for cpf in cpfs_remocao:
            inicio = time.perf_counter()
            estrutura.remover(cpf)
            fim = time.perf_counter()
            tempos_remoçao.append(fim - inicio)
            
        salvar_arquivo_res(nome_est, "remover", tempos_remoçao)

    print("\n" + "="*76)
    print("✨ Concluído com sucesso! Resultados exportados para ./relatorio/resultados/")
    print("="*76)

if __name__ == "__main__":
    rodar_benchmark()