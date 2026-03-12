import os

# Função para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

limpar_tela()

history = []
search = None
while True:
    search = str(input(f"Digite a URL da pagina:\n"))
    match search.upper():
        case "":
            break
        case "C":
            limpar_tela()
            history.clear()
            print("Histórico limpado com sucesso!!\n")
        case "H":
            limpar_tela()
            history.reverse()
            
            print(f"Histórico: \n")
            for i in range(0, len(history), 1):
                print(f"-->{history[i]}")
        case _:
            limpar_tela()
            history.append(search)


limpar_tela()

history.reverse()

print(f"Histórico: \n")
for i in range(0, len(history[0:5]), 1):
    print(f"-->{history[i]}")