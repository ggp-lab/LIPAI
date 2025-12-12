"""Exercicio 05"""

erros = []

identificador = input('Escreva um Identificador (Modelo: BR0001X): ')

if len(identificador) != 7:
    erros.append('O identificador deve conter apenas 7 caracteres')

if identificador[0:2] != 'BR':
    erros.append('O identificador deve conter no inicio as letras "BR"')

validação_numero = identificador[2:6]

if not validação_numero.isdigit():
    erros.append('O numero do identificador é inválido')
else:
    numero = int(identificador[2:6])

    if (1 > numero) or (9999 < numero):
        erros.append('O identificador possui um número inválido')

if identificador[6] != 'X':
    erros.append('O identificador possui uma letra final invalida')

if len(erros) == 0:
    print('Identificador válido')

else: 
    print('Identificador inválido')
    for erro in erros:
        print(' ', erro)