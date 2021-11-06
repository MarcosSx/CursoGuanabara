# Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cidade = str(input('Digite o nome de sua cidade:\n')).upper()
santo = cidade.split()
print(santo[0]=='SANTO')

