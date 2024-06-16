# 1) Escreva um programa que lê dois números e informa se a sua soma é par ou ímpar. Critério: se o resto da divisão do número por 2 for 0, o número é par, caso contrário é ímpar. Lembre-se do operador do python % que retorna o resto de uma divisão.
a = int(input("Escreva um número: "))
b = int(input("Escreva um número: "))
if (a+b)%2 == 0:
    print("A soma é par")
else:
    print("A soma é ímpar")

# 2) Você está criando um sistema de classificação de filmes com base nas avaliações dos usuários. Escreva um programa em Python que solicita ao usuário para inserir a avaliação de um filme em uma escala de 1 a 5. O programa deve imprimir uma mensagem correspondente à classificação do filme:
avaliação = int(input("Avalie o filme em uma escala de 1 a 5: "))
if avaliação == 5:
    print("Excelente!")
elif avaliação == 4:
    print("Muito Bom!")
elif avaliação == 3:
    print("Bom!")
elif avaliação == 2:
    print("Regular.")
elif avaliação == 1:
    print("Ruim.")

# 3) Você está desenvolvendo um programa para verificar se um ano é bissexto. Escreva um código em Python que solicita ao usuário para inserir um ano e imprime "Bissexto" se o ano for (1) divisível por 4 e não for divisível por 100, ou (2) se for divisível por 400. Caso contrário, imprima "Não Bissexto".
ano = int(input("Qual o ano atual? "))
if (ano%4 == 0 and ano&100 != 0) or ano%400 == 0:
    print("Ano bissexto")
else:
    print ("Não bissexto")

# 4) Você está implementando um sistema de entrega expressa e precisa calcular o valor do frete com base na distância e no peso do pacote. Escreva um código que solicita a distância da entrega em quilômetros e o peso do pacote em quilogramas. O programa deve calcular e imprimir o valor do frete de acordo com as seguintes regras:
distancia = int(input("Qual a distancia em Km? "))
peso = int(input("Qual o peso em Kg? "))
if distancia <=100:
    preço = 1*peso
elif 100<distancia<=300:
    preço = 1.5*peso
else:
    preço = 2*peso
if peso>10:
    preço = preço+10
print (f" Este é o preço do frete: R${preço}")
