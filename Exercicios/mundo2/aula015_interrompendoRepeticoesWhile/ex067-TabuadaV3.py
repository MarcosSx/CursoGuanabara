# Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
# digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
while True:
    print('#-#-' * 20)
    t = int(input('Digite um numero para obter sua tabuada [para parar digite um numero negativo]: '))
    if t < 0:
        break
    for n in range(0, 11):
        print(f'{t} x {n:<2} = {t * n}')
