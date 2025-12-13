"""Exercicio 03"""

calendario = {

    '1': 'Janeiro',
    '2': 'Fevereiro',
    '3': 'Março',
    '4': 'Abril',
    '5': 'Maio',
    '6': 'Junho',
    '7': 'Julho',
    '8': 'Agosto',
    '9': 'Setembro',
    '10': 'Outubro',
    '11': 'Novembro',
    '12': 'Dezembro'}

numero = input('Escreva um mes no formato númerico (ex: Janeiro = 1): ')
if numero not in calendario:
    print('Número inválido, fora do intervalo [1, 12]')
else:
    print('O mes escolhido é:', calendario[numero])

