# Escreva um script que dado uma frase conta os espaços em branco.
x=input("Escreva uma frase: ")
espaços=0
for i in range(len(x)):
    if x[i] == " ":
        espaços+=1
print(f"A quantidade de espaços na frase é: {espaços}!")