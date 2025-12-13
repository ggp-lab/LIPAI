"""Aula 05 - break e continue"""

for i in range(10):
    if i == 4:
        break
    print(i)


busca = 5
numeros = [1, 4, 9, 7, 5, 3, 2, 1, 7]
posicao = -1

contador = 0
for numero in numeros:
    print('Procurando na posicao:', contador)
    if numero == busca:
        posicao = contador
        break
        
    contador += 1

print(contador)


for i in range(len(numeros)):
    print('Procurando na posicao:', contador)
    if numeros[i] == busca:
        posicao = i
        break

print(contador)

print('---------')
for numero in numeros:
    if numero ==3:
        continue
    print(numero)
