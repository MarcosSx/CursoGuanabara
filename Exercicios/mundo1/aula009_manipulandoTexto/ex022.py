# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao to do (sem considerar espaços).
# - Quantas letras tem o primeiro nome.
frase = str(input('Digite seu nome completo:\n')).strip()
separa = frase.split()

print('Nome: {}\nMaiusculas: {}\nMinusculas:{}'.format(frase, frase.upper(), frase.lower()))
print('Quantidade de letras: {}'.format(len(frase) - frase.count(' ')))
print('Quantidade de letras no primeiro nome {}'.format(frase.find(' ')))
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))
