# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas
# listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final,
# mostre o conteúdo das três listas geradas.

lista = list()
cont_p = cont_i = 0

while True:
    lista.append(int(input('Digite um numero: ')))

    parar = ' '
    while parar not in 'SN':
        parar = input('Deseja parar? [S/N]').strip()[0].upper()
    if parar in 'S':
        break

par = lista[:]
impar = lista[:]

for pos, p in enumerate(lista):
    if p % 2 == 0:
        impar.pop(pos - cont_p)
        cont_p += 1
    else:
        par.pop(pos - cont_i)
        cont_i += 1

print(f'Lista original {lista}')
print(f'Lista de numeros pares {par}' if len(par) > 0 else 'Na lista original não tem valores pares')
print(f'Lista de numeros impares {impar}'if len(impar) > 0 else 'Na lista original não tem valores impares')
