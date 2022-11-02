lst_unidade = ['UM', 'DOIS', 'TRES', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE']
lst_dezena_simples = ['DEZ', 'ONZE', 'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO',
                      'DEZENOVE']
lst_dezena = ['VINTE', 'TRINTA', 'QUARENTA', 'CINQUENTA', 'SESSENTA', 'SETENTA', 'OITENTA', 'NOVENTA']
lst_centena = ['CENTO', 'DUZENTOS', 'TREZENTOS', 'QUATROCENTOS', 'QUINHENTOS', 'SEICENTOS', 'SETECENTOS', 'OITOCENTOS',
               'NOVECENTOS']

m = c = d = u = ''
numero = int(input('Insira um numero de 0 a 9999\n'))
milhares = numero // 1000
centenas = numero % 1000 // 100
dezenas = numero % 1000 % 100 // 10
unidades = numero % 1000 % 100 % 10 // 1

if numero == 0:
    numero_extenso = 'ZERO'
elif 9 < numero < 19:
    for i in range(numero - 9):
        numero_extenso = lst_dezena_simples[i]
elif numero == 100:
    numero_extenso = 'CEM'

if milhares != 0:
    m = lst_unidade[milhares - 1] + ' mil '
if centenas != 0:
    for i in range(centenas):
        c = lst_centena[i] + ' e '
if dezenas != 0:
    if 9 < numero % 1000 % 100 < 19:
        for i in range(numero % 1000 % 100 - 9):
            d = lst_dezena_simples[i]
    else:
        for i in range(dezenas):
            d = lst_dezena[i - 1]
        if numero % 1000 % 100 % 10 != 0:
            d += ' e '
if unidades != 0:
    u = lst_unidade[unidades - 1]

print(f'{m.lower()}{c.lower()}{d.lower()}{u.lower()}')

