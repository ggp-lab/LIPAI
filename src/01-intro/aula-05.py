""" Aula 05 - Tipos de dados"""

idade = 20
peso = 70.5

print(idade, type(idade))
print(peso, type(peso))

nome = 'Pedro'
sobrenome = 'Dos Santos'
nome_completo = nome + ' ' + sobrenome
print(nome_completo)

produto = 'Coca-Cola'

print(f'O cliente {nome} {sobrenome} comprou o {produto}')

print(nome[0], nome[-1])

print(nome.lower())
print(nome.upper())

print(1, 3, 7, 10, 'sjdbsahbd', sep ='   ')

ligado = True
print(ligado, type(ligado))

resultado = 10 == 10
print(resultado, type(resultado))

frutas = ['banana', 'uva', 'morango']
print(frutas)
print(frutas[0])
print(frutas[1])
print(frutas[2])


frutas[0] = 'banana nanica'
frutas.append('abacaxi')
print(frutas)
print(len(frutas))

for fruta in frutas:
    print(fruta.upper())


codigos = ('SP01', 'SP02', 'SP03')
print(codigos[0])

print(len(codigos))


resultado_sorteio = {10, 4, 3, 55, 9}
print(resultado_sorteio)

resultado_sorteio.add(23)
print(resultado_sorteio)


funcionario = {
    'codigo': 123,
    'nome': 'Maria da Silva',
    'salario': 7000.00
}

print(funcionario)
print(funcionario['codigo'])
print(funcionario['nome'])
print(funcionario['salario'])

print(funcionario.keys())
print(funcionario.values())

funcionario['salario'] = 9000.00
print(funcionario)