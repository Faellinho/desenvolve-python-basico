#  Faça um programa que gere aleatoriamente 20 valores inteiros entre -100 e 100 e os armazene em uma lista. Em seguida imprima na ordem estabelecida:
# A lista ordenada, sem modificar a lista original
# A lista original
# O índice do maior valor da lista
# O índice do menor valor da lista
import random
nums=[]
for i in range(20):
    nums.append (random.randint(-100, 100))
print(sorted(nums))
print(nums)
print(max(nums))
print(min(nums))
