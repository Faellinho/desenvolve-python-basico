# Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso. 
# Dica: usando listas você não precisa fazer um "if" para cada mês.
# Ex:
# Digite uma data de nascimento: 29/10/1973
# Você nasceu em  29 de Outubro de 1973.
meses_do_ano = [
    "Janeiro", "Fevereiro", "Março", "Abril",
    "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro"
]
aniversario=input("Digite sua data de aniversário: ")
aniversario=aniversario.split("/")
print(f"Você nasceu em {aniversario[0]} de {meses_do_ano[int(aniversario[1])-1]} de {aniversario[2]}.")
