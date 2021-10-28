# Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa
# Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

cores = {
    'limpa': '\33[m',
    'vermelho': '\33[1;97;41m',
    'verde': '\33[1;97;42m',
    'azul': '\33[1;97;44m',
    'amarelo': '\33[1;97;43m'
}
peso = float(input('Isira aqui o seu peso\n'))
altura = float(input('Isira aqui a sua altura \n'))
imc = peso / (pow(altura, 2))
if imc < 18.5:
    print('Seu IMC é de {:.1f}, e você está {}ABAIXO DO PESO{}'.format(imc, cores['vermelho'], cores['limpa']))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é de {:.1f}, e você está {}NO PESO IDEAL{}'.format(imc, cores['verde'], cores['limpa']))
elif imc >= 25 and imc < 30:
    print('Seu IMC é de {:.1f}, e você está {}COM SOBREPESO{}'.format(imc, cores['azul'], cores['limpa']))
elif imc >= 30 and imc < 40:
    print('Seu IMC é de {:.1f}, e você está {}COM OBESIDADE{}'.format(imc, cores['amarelo'], cores['limpa']))
else:
    print('Seu IMC é de {:.1f}, e você está {}COM OBESIDADE MORBIDA{}'.format(imc, cores['vermelho'], cores['limpa']))
