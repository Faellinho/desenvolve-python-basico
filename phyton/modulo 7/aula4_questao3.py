# Baixe o arquivo contendo o roteiro do filme brasileiro "Estômago" (link a seguir) e salve em seu computador com o nome "estomago.txt". 

# Link: https://aplauso.imprensaoficial.com.br/edicoes/12.0.813.502/12.0.813.502.txt

# Em seguida crie um script em Python que abra o arquivo para leitura e imprima: 
# O texto das primeiras 25 linhas
# O número de linhas do arquivo
# A linha com maior número de caracteres
# O número de menções aos nomes dos personagens "Nonato" e "Íria" (inclua todas as variações de maiúsculas e minúsculas e atenção para não incluir a substring "iria" se ela fizer parte de outras palavras).

import os

# Nome do arquivo
arquivo_nome = "estomago.txt"

# Função para ler o arquivo e realizar as operações
def processar_arquivo(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    # Primeiras 25 linhas
    print("Primeiras 25 linhas:")
    for linha in linhas[:25]:
        print(linha.strip())

    # Número de linhas no arquivo
    num_linhas = len(linhas)
    print("\nNúmero de linhas no arquivo:", num_linhas)

    # Linha com maior número de caracteres
    linha_maior = max(linhas, key=len)
    print("\nLinha com maior número de caracteres:")
    print(linha_maior.strip())
    print("Número de caracteres nessa linha:", len(linha_maior.strip()))

    # Número de menções aos personagens "Nonato" e "Íria"
    nonato_count = 0
    iria_count = 0
    for linha in linhas:
        palavras = linha.split()
        nonato_count += sum(1 for palavra in palavras if palavra.lower() == "nonato")
        iria_count += sum(1 for palavra in palavras if palavra.lower() == "íria")
    
    print(f"\nNúmero de menções ao personagem 'Nonato': {nonato_count}")
    print(f"Número de menções ao personagem 'Íria': {iria_count}")

# Executa a função com o arquivo especificado
processar_arquivo(arquivo_nome)
