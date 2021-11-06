# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
# Resolução com While
num = int(input('Digite um numero para saber seu fatorial: '))
print('{}! = '.format(num), end='')
fatorial = 1
while num > 0:
    print('{}'.format(num), end='')
    print(' = ' if num == 1 else ' x ', end='')
    fatorial *= num
    num -= 1
print(fatorial)

# resolução com for
# for c in range(num, 1, -1):
#     print('{} x '.format(c), end='')
#     fatorial *= c
# print('1 = {}'.format(fatorial))
