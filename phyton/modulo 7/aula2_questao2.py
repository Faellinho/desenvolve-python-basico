# Desenvolva um programa que solicite ao usuário inserir uma frase e substitua todas as ocorrências de vogal por "*".
# Ex:
# Digite uma frase: O rato roeu a roupa do rei
# Frase modificada: * r*t* r*** * r**p* d* r**
frase=input("Digite sua frase: ")
for i in range(len(frase)):
    if frase[i].lower() in "aeiou":
        frase=frase.replace(frase[i],"*")
print(frase)