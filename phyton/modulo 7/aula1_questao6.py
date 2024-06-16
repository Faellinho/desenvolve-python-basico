# Dada uma string e uma palavra objetivo, encontre todos os anagramas da palavra objetivo. Anagramas são palavras com os mesmos caracteres rearranjados.
def sao_anagramas(palavra1, palavra2):
    return sorted(palavra1) == sorted(palavra2)

# Lê a frase e a palavra objetivo
frase = input("Digite uma frase: ").lower()
palavra_objetivo = input("Escolha uma palavra em específico da frase: ").lower()

# Divide a frase em palavras usando o método split()
palavras = frase.split()

# Verifica se a palavra objetivo está na lista de palavras da frase
if palavra_objetivo not in palavras:
    print("Sua palavra não está na frase")
else:
    # Lista para armazenar os anagramas encontrados
    anagramas = []
    
    # Percorre todas as palavras da frase
    for palavra in palavras:
        if sao_anagramas(palavra, palavra_objetivo):
            anagramas.append(palavra)
    
    # Imprime os anagramas encontrados
    if anagramas:
        print(f"Anagramas da palavra '{palavra_objetivo}' na frase: {', '.join(anagramas)}")
    else:
        print(f"Não foram encontrados anagramas da palavra '{palavra_objetivo}' na frase.")