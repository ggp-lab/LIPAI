"""Aula 02 - Manipulando arquivos com Python"""

arq = open('arquivo.txt', 'w')



arq.write()
arq.writelines()

with open('arquivo.txt', 'r') as arq:
    print(next(arq))
    print(next(arq))