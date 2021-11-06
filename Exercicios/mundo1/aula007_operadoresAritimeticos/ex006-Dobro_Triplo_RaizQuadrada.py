# Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
# tambem faz a potencia do numero pow(n,2)
n = int(input('Digite um numero: '))
print('O dobro deste numero é {},\no triplo é {},\ne a raiz quadrada é {:.3f}'.format(n*2, n*3, n**(1/2)))