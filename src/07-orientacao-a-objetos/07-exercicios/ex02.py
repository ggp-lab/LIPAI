"""Exercicio 02"""

class Projeto:
    def __init__(self, codigo, titulo, responsavel):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel

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

    def __eq__(self, other):
        if isinstance(other, Projeto):
            return self.codigo == other.codigo
        return False

    def __str__(self):
        return f'Projeto[codigo={self.codigo}, titulo={self.titulo}, responsavel={self.responsavel}]'


projeto1 = Projeto.from_string("1,Laboratório de Desenvolvimento de Software,Pedro Gomes")
projeto2 = Projeto.from_string("1,Outro Título,Outro Professor")
projeto3 = Projeto.from_string("2,Projeto Web,Ana Silva")

print(projeto1)
print(projeto1 == projeto2)
print(projeto1 == projeto3)
