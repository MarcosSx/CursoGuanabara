# Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
import datetime
ano = int(input('Digita um um ano ai karay:\n'))
esteAno = datetime.date.today().year
print('este ano é bissesto' if esteAno % 4 == 0 and esteAno % 100 != 0 and esteAno % 400 != 0 else 'este ano não é bissesto')
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano Bissesto parça')
else:
    print('Não bissesto mane')

