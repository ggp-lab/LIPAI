""" I/O input and output"""

print('hello world', 'Maria', 1, True, sep='@', end='!!!!!\n')
print('hello world', 'Maria', 1, True, sep='@', end='')




arquivo = open('nomes.txt', 'w', encoding='utf-8')

print('joao@email.com',
    'maria@email.com',
    'pedro@email.com',
    file=arquivo,
    sep=';')


nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))


if idade >= 18:
    print(f'{nome}, você é maior de idade')
else:
    print(f'{nome}, você é menor de idade')

arquivo_notas = open('notas.txt', 'r', encoding='utf-8')

conteudo = arquivo_notas.read()
notas = conteudo.split(sep=';')
print(notas)

notas = [float(notas) for nota in notas]

print(notas)

media = float(notas[0]) + float(notas[1]) + float(notas[2]) / len(notas)
print()







