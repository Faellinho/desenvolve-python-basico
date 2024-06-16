# De acordo com uma pesquisa do linguista Matt Davis, o cérebro humano consegue ler palavras com as letras embaralhadas, contanto que a primeira e a última letra estejam no lugar correto. Implemente uma função chamada embaralhar_palavras() para ajudar a testar a hipótese do Matt Davis. Sua função vai receber uma frase, embaralhar as letras internas de cada palavra e retornar a frase modificada. Dica: use a biblioteca random.

# Complete o seguinte código:
import random

def embaralhar_palavras(frase):
    # Divide a frase em palavras
    palavras = frase.split()
    resultado = []

    for palavra in palavras:
        # Se a palavra tiver menos de três letras, mantenha-a como está
        if len(palavra) <= 3:
            resultado.append(palavra)
        else:
            # Embaralha as letras internas da palavra
            letras_interiores = list(palavra[1:-1])
            random.shuffle(letras_interiores)
            palavra_embaralhada = palavra[0] + ''.join(letras_interiores) + palavra[-1]
            resultado.append(palavra_embaralhada)

    # Retorna a frase modificada
    return ' '.join(resultado)

# Exemplo de uso:
frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)
# Possível saída: "Ptohyn é uma lignaugem de prarmoagãço"