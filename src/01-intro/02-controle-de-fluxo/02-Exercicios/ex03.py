"""Exercicio 03"""

identificador = input('Escreva um identificador (modelo BR0001X):')

if len(identificador) == 7:
    if identificador [0:2] == "BR":
        numero = int(identificador [2:6])

        if 1 <= numero <= 9999:
            if identificador [6] == "X":
                print('Identificador Válido!')
            else: 
                print('Identificador Inválido')
        else:
            print('Identificador inválido')

    else:
        print('Identificador inválido')


else:
    print('Identificador inválido')