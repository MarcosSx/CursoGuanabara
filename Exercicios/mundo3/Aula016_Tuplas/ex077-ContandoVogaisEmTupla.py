# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você
# deve mostrar, para cada palavra, quais são as suas vogais.
palavras = 'Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit', 'Etiam', 'tincidunt', 'eros', \
           'dignissim', 'venenatis', 'purus', 'elit', 'lacinia', 'velit', 'vestibulum'

for p in range(0, len(palavras)):
    print(f'\nNa palavra {palavras[p]} temos:', end=' ')
    for letras in palavras[p]:
        if letras.upper() in 'AEIOU':
            print(letras, end='')
