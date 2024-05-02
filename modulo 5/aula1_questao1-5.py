# 1) Desenvolva um programa em Python que peça ao usuário para inserir dois números decimais e calcule a diferença absoluta entre esses dois números. Utilize a função nativa abs para garantir que o resultado seja sempre positivo e round para arredondar o resultado para duas casas decimais.
n1=float(input())
n2=float(input())
print(round(abs(n1-n2),2))

# 2) Escreva um código que gere n valores inteiros aleatórios entre 0 e 100 e calcule a raíz quadrada da soma dos valores. Peça ao usuário o valor de n.
import math,random
n = int(input("Quantos valores? "))
for i in range (n):
    ran = random.randint(0,100)
    print(ran)
    ran = ran + ran
raiz = math.sqrt(ran)
print(f"A raiz da soma é {raiz}")

# 3) Escreva um programa em Python que utiliza a biblioteca random para gerar um número aleatório entre 1 e 10 e peça ao usuário para adivinhar o número. Forneça feedback se o palpite é muito alto, muito baixo ou correto. Interrompa a execução somente quando o usuário acertar o palpite.
while True:
    n=random.randint(0,10)
    m=int(input())
    if m == n:
        print("Você acertou!")
        break
    elif m>n:
        print("O numero é menor!")
    elif m<n:
        print("O numero é maior!")
print("Fim")

# 4) Escreva um programa em Python que utiliza a biblioteca datetime para exibir a data e hora atuais com a formatação apresentada a seguir:
from datetime import date, datetime, timezone, timedelta

# Obtendo a data atual
data_atual = date.today()
data_em_texto = data_atual.strftime('%d/%m/%Y')

# Definindo o fuso horário desejado
diferenca = timedelta(hours=-3)
fuso_horario = timezone(diferenca)

# Obtendo a hora atual ajustada ao fuso horário especificado
hora_atual = datetime.now(timezone.utc).astimezone(fuso_horario)
hora_em_texto = hora_atual.strftime('%H:%M')

# Imprimindo data e hora
print(data_em_texto)
print(hora_em_texto)

# 5) Você está trabalhando em um sistema de mensagens instantâneas, que deve permitir o uso de emojis nas conversas entre pessoas. Faça:
import emoji
print("Emojis disponíveis: ")
print("❤️ - :red_heart: ")
print("👍 - :thumbs_up: ")
print("🤔 - :thinking_face: ")
print("🥳 - :partying_face: ")
texto=input("Digite sua mensagem: ")
print (emoji.emojize(texto))
