def remover_caracteres(string):
    string = string.replace(" ", "")
    string = string.replace("-", "")
    string = string.replace(".", "")
    return string
cpf=input("Digite seu cpf: ")
cpf=remover_caracteres(cpf)
if len(cpf) != 11:
    print("Cpf Inválido")
else:
    soma=0
    for i in range(9):
        soma += (int(cpf[i]) * (10-i))
    if soma % 11 < 2:
        if int(cpf[9]) == 0:
            soma=0
            for i in range(10):
                soma += int(cpf[i] * (11-i))
            if soma % 11 < 2:
                if int(cpf[10]) == 0:
                    print("Cpf Válido")
                else:
                    print("Cpf Inválido")
            elif soma % 11 >= 2:
                if int(cpf[10]) == (11-(soma % 11)):
                    print("Cpf Válido")
                else:
                    print("Cpf Inválido")
        else:
            print("Cpf Inválido")
    elif soma % 11 >= 2:
        if int(cpf[9]) == (11-(soma % 11)):
            soma=0
            for i in range(10):
                soma += (int(cpf[i]) * (11-i))
            if soma % 11 < 2:
                if int(cpf[10]) == 0:
                    print("Cpf Válido")
                else:
                    print("Cpf Inválido")
            elif soma % 11 >= 2:
                if int(cpf[10]) == (11-(soma % 11)):
                    print("Cpf Válido")
                else:
                    print("Cpf Inválido")
        else:
            print("Cpf Inválido")