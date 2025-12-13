"""Aula 02 - Tuplas"""

nomes = ('Maria', 'Pedro', 'João')
print(nomes, type(nomes))

print(nomes[0])
print(nomes[0:2])
print(nomes[:2])
print(nomes[1:])


#nomes[0] = 'Maria da Silva'


for nome in nomes:
    print(nome)

for i in range(len(nomes)):
    print(nomes[i])


nomes2 = 'Ana', 'Amélia', 'Marcos'
print(nomes2, type(nomes2))


nome1 = nomes2[0]
nome2 = nomes2[1]
nome3 = nomes2[2]

nome1, nome2, nome3 = nomes2
print(nome1, nome2, nome3)


todos_nomes = nomes + nomes2
print(todos_nomes, type(todos_nomes))


