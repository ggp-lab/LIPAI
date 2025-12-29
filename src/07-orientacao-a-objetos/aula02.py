"""Aula 02 - Atributos de classe e instância"""

class Pessoa:
    especie = 'Humano'

    def __init__(self, nome, email):
            self.nome = nome
            self.email = email


pessoa1 = Pessoa('Maria da Silva', 'maria@email.com')
pessoa2 = Pessoa('João Santos', 'joao@email.com')
pessoa3 = Pessoa('Pedro Santos', 'pedro@email.com')

pessoa1.especie = 'Alienigena'

Pessoa.especie = 'Alienigena do passado'

print(pessoa1.nome, pessoa1.email, pessoa1.especie)
print(pessoa2.nome, pessoa2.email, pessoa2.especie)
print(pessoa3.nome, pessoa3.email, pessoa3.especie)

print(Pessoa.especie)





