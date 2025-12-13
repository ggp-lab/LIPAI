"""Exercico 01"""

numeros = input('Escreva os números: ')

lista_numeros = numeros.split(' ')

for i in range(len(lista_numeros)):
    lista_numeros[i] = float(lista_numeros[i])

if len(lista_numeros) < 3:
    print('Erro, o usuario deve escrever pelo menos 3 números') 
else:
    menor_numero = lista_numeros[0]
    maior_numero = lista_numeros[0]


    for i in range(len(lista_numeros)):
        if menor_numero > lista_numeros[i]:
            menor_numero = lista_numeros[i]
        elif maior_numero < lista_numeros[i]:
            maior_numero = lista_numeros[i]
    

    print('O maior número é: ', maior_numero)
    print('----------')
    print('O menor número é: ', menor_numero)
    print('----------')
    print('A lista é: ', lista_numeros)






