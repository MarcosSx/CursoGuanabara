# Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10
# primeiros termos dessa progressão.
#Resolução do GUANABARA

# primeiro = int(input('Primeiro termo: '))
# razão = int(input('Razão: '))
# décimo = primeiro + (10 - 1) * razão
# for c in range(primeiro, décimo + razão, razão):
#     print('{} '.format(c), end='→ ')
# print('ACABOU')

num = float(input('Digite o primeiro termo da PA: '))
razao = float(input('Digite a razão dessa PA: '))
print('primeiro termo = {}'.format(num), end=' → ')
for i in range(1, 10, 1):
    pa = num + razao
    print(pa, end=' → ')
    num += razao
print('Fim')


