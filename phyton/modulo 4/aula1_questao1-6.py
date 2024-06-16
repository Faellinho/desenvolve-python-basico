#  1) Transforme em código o fluxograma a seguir
x = int(input())
if x>5:
    print("X é maior que 5")
print("Fim")

#  2) Transforme em código o fluxograma a seguir
n = int(input())
cont = 0
while n<cont:
    cont = cont + 1
    print(cont)
print("Fim")

#  3) Transforme em código o fluxograma a seguir
n1 = int(input())
n2 = int(input())
n3 = int(input())
m = (n1+n2+n3)/3
if m>=60:
    print("aprovado")
elif m >= 40:
    print ("Recuperação")
else:
    print("Reprovado")
print("Fim")

# 4) Transforme em código o fluxograma a seguir
n = int(input())
maior = 0
while n >0:
    x = int(input())
    while x > maior:
        maior = x
    n = n -1
print(maior)

# 5) Um instituto realizou uma pesquisa de público e precisa calcular a média de idade dos respondentes. Escreva um programa que leia um inteiro N com a quantidade de respondentes e em seguida leia as N idades de cada respondente. Ao final, imprima a média das idades.
N = int(input("Qual a quantidade de respondentes? "))
seq = 0 
dividendo = 0
while N!=seq:
    dividendo = dividendo + int(input("Qual a idade deste respondente"))
    seq = seq +1
media = dividendo/N
print(f"A media das idades é {media}")

# 6) Exercício de maratona:
n = int(input("Quantos experimentos foram realizados? "))
cont = 0
soma_sapo,soma_rato,soma_coelho = 0,0,0
while cont< n:
    quantia = int(input())
    tipo = input()

    if tipo == "S":
        soma_sapo += quantia
    elif tipo == "C":
        soma_coelho += quantia
    elif tipo == "R":
        soma_rato+=quantia

    cont += 1
print (f"Total de Cobaias é: {soma_sapo+soma_coelho+soma_rato}")
print (f"Total de Ratos é: {soma_rato}")
print (f"Total de Coelhos é: {soma_coelho}")
print (f"Total de Sapos é: {soma_sapo}")