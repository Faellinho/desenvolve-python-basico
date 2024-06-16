
# pergunta se elas possuem idade para entrar
chris = int(input("Qual a idade de chris? "))
juliana = int(input("Qual a idade de juliana? "))

# imprime True caso elas sejam aptas a entrar
print(chris > 17 and juliana > 17)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~

# pergunta se elas possuem idade para entrar
chris = int(input("Qual a idade de chris? "))
juliana = int(input("Qual a idade de juliana? "))
# imprime True caso elas sejam aptas a entrar
print(chris > 17 or juliana > 17)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~

# pergunta a idade, quantas vezes ja jogou, e quantas vezes ja venceu
idade = int(input("Qual a sua idade? "))
jogos = input("Você já jogou 3 jogos de tabuleiro ou mais?(True-sim)(False-não)")
vencer = int(input("Quantas vezes você já venceu um jogo? "))
# imprime se o participante tem consdiçoes para participar
print((idade >= 16 and idade <= 18 ) and (jogos == "True") and (vencer >= 1))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~

# pergunta a classe do personagem seguido de seus atributos
classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ")
força = int(input ("Digite os pontos de força (de 1 a 20): "))
magia = int(input ("Digite os pontos de magia (de 1 a 20): "))
# imprime True caso os pontos de atributo sejam consistentes
print ("Pontos de atributo consistentes com a classe escolhida:")
print ((classe == "mago" and força <= 10 and magia >=15) or (classe == "guerreiro" and força >= 15 and magia <= 10 ) or (classe == "arqueiro" and 5>força<15 and 5>magia<15))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~

# pergunta o genero, quantos anos trabalhado e a idade
genero = input("Qual seu genero(M ou G)? ")
trabalhado = int(input("Quantos anos você trabalhou? "))
anos = int(input("Qual a sua idade? "))
# imprime true caso cumpra as regras para aposentar
print ((genero == "F" and anos > 60) or (genero == "M" and anos > 65) or (trabalhado >= 30) or (anos >= 60 and trabalhado >= 25))