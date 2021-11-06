# Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a
# média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
# quer ou não continuar a digitar valores.

continuar = 'S'
soma = quant = media = menor = maior = 0
while continuar not in 'Nn':
    if continuar in 'Ss':
        num = int(input('Digite um numero inteiro: '))
        soma += num
        quant += 1
        if quant == 1:
            maior = menor = num
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num
        continuar = str(input('Deseja continuar [S/N]: '))
    elif continuar in 'Nn':
        pass
    else:
        print('Opção invalida')
        continuar = str(input('Deseja continuar [S/N]: '))
media = soma / quant
print('\nO maior numero digitado foi {} e o menor foi {}'.format(maior, menor))
print('Voce digitou {} numeros. E a media entre eles é de {}'.format(quant, media))
