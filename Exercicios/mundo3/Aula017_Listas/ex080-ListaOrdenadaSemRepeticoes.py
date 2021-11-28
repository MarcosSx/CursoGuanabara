# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma
# lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
lista = list()
for i in range(0, 5):
    n = int(input(f'Digite {i + 1}º numero: '))
    if i == 0 or n > lista[-1]:
        lista.append(n)
        print(f'Adicionando numero {n} no final da lista' if i > 0 else f'Adicionando o primeiro numero')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionando numero {n} na posição {pos} da lista')
                break
            pos += 1
print(lista)

