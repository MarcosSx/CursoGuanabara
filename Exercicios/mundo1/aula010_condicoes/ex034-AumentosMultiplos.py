# Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
cores = {'limpa': '\33[m',
         'branco': '\33[7;34;107m',
         'vermelho': '\33[7;30;41m',
         'verde': '\33[7;30;42m'
         }
salario = float(input('Digite seu salario para consultar o aumento\n'))
aumento = salario * 0.15 + salario if salario <= 1250.00 else salario * 0.10 + salario
quantAumento = 15 if salario <= 1250 else 10
print('Seu salario era de {}R${:.2f}{} e aumentou {}{}%{} agora seu salario é {}R${:.2f}{}'.format(cores['vermelho'],
                                                                                               salario, cores['limpa'],
                                                                                               cores['branco'],
                                                                                               quantAumento,
                                                                                               cores['limpa'],
                                                                                               cores['verde'], aumento,
                                                                                               cores['limpa']))
