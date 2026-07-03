import os
import glob
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Configuração de pastas (alinhado com o seu script original)
PASTA_RESULTADOS = "relatorio/resultados"
PASTA_GRAFICOS   = "relatorio/graficos"

# Dicionário para mapear as anotações Big-O baseado no tipo de arquivo
# CORREÇÃO: Adicionados 'adicionar' e 'remover' para bater com as suas novas palavras-chave
ANOTACOES = {
    'insercao': "End. Livre: O(1) méd. / O(n) pior\nEncadeada BST: O(1) méd. / O(log n) no pior balde",
    'adicionar': "End. Livre: O(1) méd. / O(n) pior\nEncadeada BST: O(1) méd. / O(log n) no pior balde",
    'busca':    "End. Livre: O(1) méd. / O(n) pior\nEncadeada BST: O(1) méd. / O(log n) no pior balde",
    'buscar':   "End. Livre: O(1) méd. / O(n) pior\nEncadeada BST: O(1) méd. / O(log n) no pior balde",
    'remocao':  "End. Livre: O(1) méd. / O(n) pior\nEncadeada BST: O(1) méd. / O(log n) no pior balde",
    'remover':  "End. Livre: O(1) méd. / O(n) pior\nEncadeada BST: O(1) méd. / O(log n) no pior balde",
}

def ler_arquivo_res(caminho_arquivo: str) -> dict:
    """Lê o arquivo .res no formato 'Nome-Algoritmo;N' seguido pelos tempos."""
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        linhas = [linha.strip() for linha in f if linha.strip()]
    
    if not linhas:
        raise ValueError(f"O arquivo {caminho_arquivo} está vazio.")
        
    # Processa a primeira linha (ex: Hash-Busca-EncadeadaBST;9998)
    cabecalho = linhas[0].split(";")
    identificador = cabecalho[0]
    n_max = int(cabecalho[1])
    
    # Processa os tempos (linhas restantes)
    tempos = [float(tempo) for tempo in linhas[1:]]
    
    return {
        'identificador': identificador,
        'n_max': n_max,
        'tempos': tempos
    }

def gerar_grafico_comparativo(titulo_grafico: str, palavra_chave_operacao: str, arquivos_res: list):
    """Gera um gráfico comparativo baseado em uma lista de arquivos .res fornecidos."""
    os.makedirs(PASTA_GRAFICOS, exist_ok=True)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Paleta de cores e marcadores idênticos ao modo legado/padrão do seu script
    cores = ['#2563EB', '#10B981', '#DC2626', '#9333EA', '#F59E0B']
    marcadores = ['o', '^', 's', 'D', 'x']
    
    for i, caminho_arq in enumerate(arquivos_res):
        try:
            dados = ler_arquivo_res(caminho_arq)
        except Exception as e:
            print(f"⚠ Erro ao ler {caminho_arq}: {e}")
            continue
            
        qtd_pontos = len(dados['tempos'])
        if qtd_pontos == 0:
            continue
            
        # Lógica original para reconstruir os passos do eixo X (ns)
        passo = dados['n_max'] // qtd_pontos
        ns = [passo * j for j in range(1, qtd_pontos + 1)]
        
        # Escolha de cor e marcador
        cor = cores[i % len(cores)]
        marcador = marcadores[i % len(marcadores)]
        
        # Plota a linha usando o 'identificador' extraído de dentro do arquivo como legenda
        ax.plot(ns, dados['tempos'], color=cor, linestyle='-',  
                marker=marcador, markersize=4, linewidth=2.5, 
                label=dados['identificador'])

    # Customização estética (Idêntica ao seu código)
    ax.set_xlabel("Tamanho da entrada (n)", fontsize=14)
    ax.set_ylabel("Tempo médio (ms)",       fontsize=14)
    ax.set_title(titulo_grafico, fontsize=15, fontweight='bold')
    
    # Legenda fixa no Canto Superior Direito
    ax.legend(fontsize=12, loc='upper right')
    
    # Grid e formatação do Eixo Y
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.5f'))

    # Adiciona a caixa de texto Big-O no Canto Superior Esquerdo se mapeado
    anotacao = ANOTACOES.get(palavra_chave_operacao.lower(), "")
    if anotacao:
        ax.annotate(
            anotacao,
            xy=(0.02, 0.96), xycoords='axes fraction',
            ha='left', va='top', fontsize=10.5,
            bbox=dict(boxstyle='round,pad=0.4', fc='lightyellow', ec='gray', alpha=0.85),
        )

    # Salva o arquivo final tratando o nome
    nome_saida = f"{PASTA_GRAFICOS}/{titulo_grafico.replace(' ', '_').replace('–','').replace('  ',' ')}.png"
    plt.tight_layout()
    plt.savefig(nome_saida, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✔ Gráfico salvo com sucesso em: {nome_saida}")


if __name__ == "__main__":
    arquivos_para_plotar = [
        "relatorio/resultados/tabela_hash_arvore_binaria_adicionar.res", # [0]
        "relatorio/resultados/tabela_hash_linear_adicionar.res",         # [1]

        "relatorio/resultados/tabela_hash_arvore_binaria_buscar.res",    # [2]
        "relatorio/resultados/tabela_hash_linear_buscar.res",            # [3]

        "relatorio/resultados/tabela_hash_arvore_binaria_remover.res",   # [4]
        "relatorio/resultados/tabela_hash_linear_remover.res"            # [5]
    ]
    
    # Gráfico 1: Pega os índices 0 e 1
    gerar_grafico_comparativo(
        titulo_grafico="Tabela Hash – Adicionar", 
        palavra_chave_operacao="adicionar", 
        arquivos_res=arquivos_para_plotar[0:2] 
    )
    
    # Gráfico 2: Pega os índices 2 e 3
    gerar_grafico_comparativo(
        titulo_grafico="Tabela Hash – Busca", 
        palavra_chave_operacao="busca", 
        arquivos_res=arquivos_para_plotar[2:4]
    )

    # Gráfico 3: Pega os índices 4 e 5
    gerar_grafico_comparativo(
        titulo_grafico="Tabela Hash – Remover", 
        palavra_chave_operacao="remover", 
        arquivos_res=arquivos_para_plotar[4:6]
    )