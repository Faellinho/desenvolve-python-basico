# Faça um programa que leia um número de celular e, caso o número tenha apenas 8 dígitos, acrescente o 9 na frente. Caso o número já tenha 9 dígitos, verifique se o primeiro dígito é 9. Adicione o separador "-" na sua impressão.
numero = input("Digite seu numero de telefone: ")
# Remove todos os espaços em branco
numero = numero.replace(" ", "")
if "-" not in numero:
    if len(numero) == 8:
        numero = "9"+numero
        numero = numero[:5]+"-"+numero[5:]
        print (numero)
    elif len(numero) == 9:
        if numero[0] != 9:
            print("número inválido")
        else:
            numero = numero[:5]+"-"+numero[5:]
            print (numero)
    else:
        print("número inválido")
elif "-" in numero[5] and len(numero)==10 and numero[0]==9:
    print (numero)
elif "-" in numero[4] and len(numero)==9:
    numero = "9"+numero
    print (numero)
else:
    print("número inválido")