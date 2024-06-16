# 1) Escreva um script em Python que solicita do usuário uma quantidade indefinida de números inteiros (pelo menos 4 valores), os armazena em uma lista e, usando fatiamento de listas, imprima:
# A lista original
# Os 3 primeiros elementos
# Os 2 últimos elementos
# A lista invertida (do fim para o começo)
# Os elementos de índice par (0, 2, 4 … )
# Os elementos de índice ímpar (1, 3, 5, … )
import random
x=random.randint(4,10)
lista1=[]
print(f"Digite {x} numeros:")
for i in range(x):
    lista1.append (int(input()))
# Imprime a lista original
print("Lista original:", lista1)

# Imprime os 3 primeiros elementos. Corrigir para incluir o terceiro elemento.
print("Os 3 primeiros elementos:", lista1[:3])

# Imprime os 2 últimos elementos. Ajustar para incluir o último elemento.
print("Os 2 últimos elementos:", lista1[-2:])

# Imprime a lista invertida (do fim para o começo)
print("Lista invertida:", lista1[::-1])

# Imprime os elementos de índice par (0, 2, 4, ...)
print("Elementos de índice par:", lista1[::2])

# Imprime os elementos de índice ímpar (1, 3, 5, ...)
print("Elementos de índice ímpar:", lista1[1::2])
