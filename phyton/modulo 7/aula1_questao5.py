# Implemente um código que leia uma string do usuário e imprima quantas vogais existem na frase e quais os seus índices da string. Dica: letra in "aeiou". Exemplo:
x=input("digite uma string: ")
vogais=0
for i in range(len(x)):
    if x[i] in "aeiou":
        vogais+=1
print(f"a quanrtidade de vogais é: {vogais}")
for i in range(len(x)):
    if x[i] in "aeiou":
        print("Indice: %d, vogal: %s" % (i,x[i]))

    