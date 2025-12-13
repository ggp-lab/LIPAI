"""Exercicio 02"""

notas = input('Escreva as notas: ')
lista_nota = notas.split(',')
lista_notas_revisadas = []


for nota in lista_nota:
    notas_revisada = float(nota)
    lista_notas_revisadas.append(notas_revisada)

soma = 0

for nota in lista_notas_revisadas:
    soma = soma + nota

media = (soma) / len(lista_notas_revisadas)

print('A media das notas é: ' , media)

NM = 6.0

if media >= NM:
    print('Situação do aluno: Aprovado')
elif 4.0 <= media < NM:
    print('Situação do aluno: Recuperação')
else: 
    print('Situação do aluno: Reprovado') 