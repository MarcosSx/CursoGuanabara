# Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Insira uma frase:\n')).upper().strip()
print('A quantidade de A que aparece na frase é: {}'.format(frase.count('A')))
print('A primeira letra A esta na posição: {}'.format(frase.find('A') + 1))
print('A ultima aparição da letra A é em: {}'.format(frase.rfind('A') + 1))
