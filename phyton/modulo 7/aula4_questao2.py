# Escreva um script que leia o arquivo salvo no exercício anterior e salva em um novo arquivo "palavras.txt", removendo todos os espaços em branco e caracteres não alfabéticos, e separando cada palavra em uma linha. Ao final, imprima o conteúdo do arquivo "palavras.txt".
# Ex:
# Bom
# dia
# meu
# nome
# é
# Davi

import os

# Define o nome dos arquivos
arquivo_frase = "frase.txt"
arquivo_palavras = "palavras.txt"

# Função para verificar se o caractere é uma letra
def is_alpha(c):
    return c.isalpha() or c in 'ÁáÀàÂâÃãÄäÅåÆæÇçÉéÈèÊêËëÍíÌìÎîÏïÐðÑñÓóÒòÔôÕõÖöØøÚúÙùÛûÜüÝýÞþß'

# Lê o conteúdo do arquivo "frase.txt"
with open(arquivo_frase, "r") as arquivo:
    conteudo = arquivo.read()

# Processa o conteúdo para remover caracteres não alfabéticos e separa as palavras
palavras = []
palavra_atual = []

for char in conteudo:
    if is_alpha(char):
        palavra_atual.append(char)
    elif palavra_atual:
        palavras.append("".join(palavra_atual))
        palavra_atual = []

# Adiciona a última palavra, se existir
if palavra_atual:
    palavras.append("".join(palavra_atual))

# Salva as palavras no arquivo "palavras.txt", uma por linha
with open(arquivo_palavras, "w") as arquivo:
    for palavra in palavras:
        arquivo.write(palavra + "\n")

# Lê e imprime o conteúdo do arquivo "palavras.txt"
with open(arquivo_palavras, "r") as arquivo:
    conteudo_palavras = arquivo.read()

print(conteudo_palavras)
