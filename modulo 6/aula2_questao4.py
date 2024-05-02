# Crie um programa em Python que receba duas listas de números do usuário, podendo cada lista ter uma quantidade diferente de valores. Em seguida, combine essas duas listas de forma alternada para formar uma terceira lista. Intercale os elementos até o final da primeira lista, adicionando ao final os elementos remanescentes da maior lista.
# Exemplo de interação via terminal (entradas em negrito):
# Digite a quantidade de elementos da lista 1: 4
# Digite os 4 elementos da lista 1:
# 1
# 2
# 3
# 4
# Digite a quantidade de elementos da lista 2: 6
# Digite os 6 elementos da lista 2:
# 5
# 6
# 7
# 8
# 9
# 10
# Lista intercalada: 1 5 2 6 3 7 4 8 9 10

print("Digite quantos números sua lista 1 vai ter: ")
x=int(input())
lista1=[]
lista2=[]
lista_intercalada=[]
print("Digite os numeros da lista: ")
for i in range (x):
    elemento1=int(input())
    lista1.append(elemento1)

print("Digite quantos números sua lista 2 vai ter: ")
y=int(input())
print("Digite os numeros da lista: ")
for u in range (y):
    elemento2=int(input())
    lista2.append(elemento2)

tamanho_max = max(len(lista1), len(lista2))  # Calcula o tamanho máximo entre as duas listas.

# Percorre de 0 até o tamanho máximo.
for i in range(tamanho_max):
    # Adiciona o elemento da lista 1 à lista intercalada, se ainda houver elementos na lista 1.
    if i < len(lista1):
        lista_intercalada.append(lista1[i])
    # Adiciona o elemento da lista 2 à lista intercalada, se ainda houver elementos na lista 2.
    if i < len(lista2):
        lista_intercalada.append(lista2[i])

print(lista1)
print(lista2)
print(lista_intercalada)
