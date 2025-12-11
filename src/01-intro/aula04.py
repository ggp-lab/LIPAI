""" Aula 04 - Variaveis, constantes e literais"""

numero = 10
print(numero)
print(type(numero))


numero = 20
print(numero)

nome, idade, endereco = 'Maria', 20, 'Rua das ...'
print(nome, idade, endereco)

nome = 'Maria'
idade = 20
endereco = 'Rua das ...'

print(nome, idade, endereco)

nome1 = nome2 = nome3 = 'João'
print(nome1, nome2, nome3)

nome2 = 'Pedro'
print(nome1, nome2, nome3)

id_funcionario = 209
salario_funcionario = 5000.50
print(id_funcionario, salario_funcionario)

PI = 3.14
MAIORIDADE_PENAL = 18
MAIORIDADE_CIVIL = 21
print(PI, MAIORIDADE_CIVIL, MAIORIDADE_PENAL)

idade = 27
print(idade)
print(27)

print(10, type(10))
print(-10, type(-10))
print(10.5, type(10.5))

print('Maria', type('Maria'))
print("Maria", type("Maria"))
print("John's House")
print('O filme estava "excelente')

print(True, type(True))
print(False, type(False))

print(None, type(None))



numeros = [1, 3, 5]
print(numeros, type(numeros))

emails = ('joao@email.com', 'Maria@email.com')
print(emails, type(emails))

nomes = {'maria', 'joão', 'pedro', 'maria'}
print(nomes, type(nomes))

aluno ={
    'prontuario' : 123456,
    'nome' : 'Maria da Silva',
    'idade': 34
}