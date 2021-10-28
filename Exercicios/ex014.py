# Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para
# graus Fahrenheit.
celcius = float(input('Coloque a temperatura em graus celcius: '))
fahrenheit = (celcius * (9/5) + 32)
kelvin = celcius + 273.15
print('{}º celcius convertido para {:.2f} fahrenheits , e {:.2f} kelvins'.format(celcius, fahrenheit, kelvin))