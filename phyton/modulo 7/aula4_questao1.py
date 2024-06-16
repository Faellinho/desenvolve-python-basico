# Escreva um script Python que solicita uma frase do usuário e a salve em um arquivo chamado "frase.txt" no mesmo local do seu script. Imprima em seguida o caminho completo do arquivo salvo.
# Ex: 
# Digite uma frase: Bom dia, meu nome é Davi.
# Frase salva em /Users/laranjeira/python-basico/frase.txt
import os  # Importa o módulo os, que fornece funções para interagir com o sistema operacional

# Solicita uma frase do usuário e armazena a entrada na variável 'frase'
frase = input("Digite uma frase: ")

# Define o nome do arquivo onde a frase será salva
nome_arquivo = "frase.txt"

# Abre o arquivo em modo de adição ("a" para append), que adiciona conteúdo ao final do arquivo sem apagar o conteúdo existente
# O 'with' statement garante que o arquivo será corretamente fechado após a escrita
with open(nome_arquivo, "a") as arquivo:
    # Escreve a frase no arquivo, seguida por uma nova linha (\n) para garantir que cada nova frase comece em uma nova linha
    arquivo.write(frase + "\n")

# Usa os.path.abspath para obter o caminho absoluto do arquivo
# Isso converte o caminho relativo do arquivo em um caminho completo a partir da raiz do sistema de arquivos
caminho_completo = os.path.abspath(nome_arquivo)

# Imprime uma mensagem informando ao usuário que a frase foi salva, incluindo o caminho completo do arquivo
print(f"Frase salva em {caminho_completo}")