# Escreva um programa que solicita o nome do usuário e o imprime em forma de escada, como indicado no exemplo a seguir.
x=input("Digite um nome: ")
x=x.upper()
for i in range(len(x)):
    print (x[:i+1])
    # o dois pontos foi adicionado para fazer um "fatiamento" desde a primeira letra até a letra do indice e o +1 foi adicionado para imprimir o nome completo no final
