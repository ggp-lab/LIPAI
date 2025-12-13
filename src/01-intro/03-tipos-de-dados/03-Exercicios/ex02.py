"""Exercicio 02"""


calendario = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

numero = input('Escreva um mes do ano em formato númerico (ex: Janeiro = 1): ')

numero_revisado = int(numero)

if numero_revisado < 1 or numero_revisado > 12:
    print('Número inválido, fora do intervalo [1, 12]')
else:
    numero_revisado = numero_revisado - 1
    print('O mes escolhido é: ', calendario[numero_revisado])
