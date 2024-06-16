# Solicite uma frase do usuário e usando compreensão de listas imprima:
# A lista de vogais da frase, ordenada alfabeticamente
# A lista de consoantes da frase
# Exemplo:
# Digite uma frase: Eu gosto de programar em Python
# Vogais: ['a', 'a', 'e', 'e', 'o', 'o', 'o', 'o', 'u']
# Consoantes: ['E', 'g', 's', 't', 'd', 'p', 'r', 'g', 'r', 'm', 'r', 'm', 'P', 'y', 't', 'h', 'n']

x=input()

vogais = 'aeiouAEIOU'
consoantes = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

lista_vogais = sorted([char for char in x if char in vogais])
lista_consoantes = [char for char in x if char in consoantes]

print(f"Vogais: {lista_vogais}")
print(f"Consoantes: {lista_consoantes}")