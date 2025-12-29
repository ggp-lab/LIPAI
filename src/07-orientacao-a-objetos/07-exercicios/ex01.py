"""Exercicio 01"""

class Aluno:
    def __init__(self, prontuario, nome, email):
        self.prontuario = prontuario
        self.nome = nome
        self.email = email

    @classmethod
    def from_string(cls, dados):
        prontuario, nome, email = dados.split(",")
        return cls(prontuario, nome, email)

    @property
    def prontuario(self):
        return self._prontuario

    @prontuario.setter
    def prontuario(self, valor):
        if not valor:
            raise ValueError("Prontuário não pode ser vazio ou nulo")
        self._prontuario = valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not valor:
            raise ValueError("Nome não pode ser vazio ou nulo")
        self._nome = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if not valor:
            raise ValueError("Email não pode ser vazio ou nulo")
        self._email = valor

    def __eq__(self, other):
        if isinstance(other, Aluno):
            return self.prontuario == other.prontuario
        return False

    def __hash__(self):
        return hash(self.prontuario)

    def __str__(self):
        return f'Aluno[prontuario={self.prontuario}, nome={self.nome}, email={self.email}]'


aluno1 = Aluno.from_string("SP0101,João da Silva,joao@email.com")
aluno2 = Aluno.from_string("SP0101,João Silva,joao.silva@email.com")
aluno3 = Aluno.from_string("SP0202,Maria Souza,maria@email.com")

print(aluno1)
print(aluno1 == aluno2)
print(aluno1 == aluno3)
