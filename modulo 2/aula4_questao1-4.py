# Pergunta para descobrir o comprimento e largura do terreno.
comprimento = int(input("qual o comprimento do terreno"))
largura = int(input("qual a largura do terreno"))

# # Formula da área.
area_m2 = comprimento * largura

# # divisão do preço do terreno pelo tamanho em m2 para definir o preço de cada metro quadrado.
preco_m2 =  512490.50 / 250

# # Formula usando a constante do preço de cada m2 pelo tamanho dito pela pessoa, seguiiodo da impressão do valor.
preco_total = preco_m2 * area_m2
print (preco_total)

# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# # Pergunta ao usuario qual será a temperatura a ser convertida
F = int(input("Qual a temperatura em Fahrenheit: "))
# # Formula para conversão
C = (F - 32) * (5/9)
# # Impressão do resultado
print(f"Essa é a temperatura em Celcius: {C}")

# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# # Sequencia de perguntas
p1 = input("Digite o nome do produto 1: ")
pr1 = int(input("Digite o valor do produto 1: "))
q1 = int(input("Digite a quantidade do produto 1: "))
p2 = input("Digite o nome do produto 2: ")
pr2 = int(input("Digite o valor do produto 2: "))
q2 = int(input("Digite a quantidade do produto 2: "))
p3 = input("Digite o nome do produto 3: ")
pr3 = int(input("Digite o valor do produto 3: "))
q3 = int(input("Digite a quantidade do produto 3: "))

# # Soma do valor total e impressão do resultado
valor_total = (pr1*q1)+(pr2*q2)+(pr3*q3)
print (f"Total: R${valor_total}")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Pergunta o valor
valor = int(input("Digite o valor: "))

# Calcula a divisão em notas
cem = int(valor/100)
cinquenta = int((valor-(cem*100))/50)
vinte = int((valor-(cem*100)-(cinquenta*50))/20)
dez = int((valor-(cem*100)-(cinquenta*50)-(vinte*20))/10)
cinco = int((valor-(cem*100)-(cinquenta*50)-(vinte*20)-(dez*10))/5)
dois = int((valor-(cem*100)-(cinquenta*50)-(vinte*20)-(dez*10)-(cinco*5))/2)
um = int((valor-(cem*100)-(cinquenta*50)-(vinte*20)-(dez*10)-(cinco*5)-(dois*2))/1)

# Imprime todas as notas que serão divididas
print(f"{cem} nota(s) de R$100,00")
print(f"{cinquenta} nota(s) de R$50,00")
print(f"{vinte} nota(s) de R$20,00")
print(f"{dez} nota(s) de R$10,00")
print(f"{cinco} nota(s) de R$5,00")
print(f"{dois} nota(s) de R$2,00")
print(f"{um} moedaa(s) de R$1,00")
