# Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
# será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

lado1 = float(input('Digite o primeiro lado do triangulo\n>>'))
lado2 = float(input('Digite o segundo lado do triangulo\n>>'))
lado3 = float(input('Digite o terceiro lado do triangulo\n>>'))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Você formou um triangulo ▲ ', end='')
    if lado1 == lado2 == lado3:
        print('EQUILATERO')
    elif lado1 != lado2 != lado3 != lado1:
        print('ESCALENO')
    else:
        print('ISÓCELES')
else:
    print('Você não formou um triangulo!')
