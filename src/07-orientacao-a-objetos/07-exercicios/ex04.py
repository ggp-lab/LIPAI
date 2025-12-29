"""Exercicio 04"""

class Projeto:
    def __init__(self, codigo, titulo, responsavel):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel
        self.participacoes = []

    @classmethod
    def from_string(cls, dados):
        codigo, titulo, responsavel = dados.split(",")
        return cls(codigo, titulo, responsavel)

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if valor is None or valor == "":
            raise ValueError("Código não pode ser vazio ou nulo")
        self._codigo = int(valor)

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, valor):
        if not valor:
            raise ValueError("Título não pode ser vazio ou nulo")
        self._titulo = valor

    @property
    def responsavel(self):
        return self._responsavel

    @responsavel.setter
    def responsavel(self, valor):
        if not valor:
            raise ValueError("Responsável não pode ser vazio ou nulo")
        self._responsavel = valor

    def add_participacao(self, participacao):
        self.participacoes.append(participacao)

    def __eq__(self, other):
        if isinstance(other, Projeto):
            return self.codigo == other.codigo
        return False

    def __str__(self):
        return (
            f'Projeto[codigo={self.codigo}, '
            f'titulo={self.titulo}, '
            f'responsavel={self.responsavel}, '
            f'participacoes={len(self.participacoes)}]'
        )
