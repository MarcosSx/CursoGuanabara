import string

a = string.printable
chave = 5
mensagem = str(input('PassWord: '))
n = len(a)
cifrada = ''

for letra in mensagem:
    indice = a.index(letra)
    nova_letra = a[(indice + chave) % n]
    cifrada += nova_letra

print(cifrada)
