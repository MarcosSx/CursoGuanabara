import string

letras = string.printable
alpha = list()

for l in letras:
    alpha.append(l)

chave = 5
mensagem = str(input('PassWord: ')).strip()

n = len(alpha)
cifrada = ''

for letra in mensagem:
    indice = alpha.index(letra)
    nova_letra = alpha[(indice + chave) % n]
    cifrada += nova_letra

print(cifrada)