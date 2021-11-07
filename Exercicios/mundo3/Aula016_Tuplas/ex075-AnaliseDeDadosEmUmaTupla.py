# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final,
# mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

num = int(input('1º Numero: ')), int(input('2º Numero: ')), int(input('3º Numero: ')), int(input('4º Numero: '))
print(num)
if num.count(9) > 0:
    print(f'O numero 9 apareceu {num.count(9)} vezes')
else:
    print('O numero 9 não foi digitado')
if 3 in num:
    print(f'O numero 3 apareceu na posição {num.index(3)+1}')
else:
    print('O numero 3 não foi digitado')
print(f'Estes são os numeros pares: ', end='')
for p in range(len(num)):
    if num[p] % 2 == 0:
        print(f'{num[p]} ', end='')