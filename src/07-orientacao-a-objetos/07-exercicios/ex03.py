"""Exercicio 03"""

class Participacao:
    def __init__(self, codigo, data_inicio, data_fim, aluno, projeto):
        self.codigo = codigo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = aluno
        self.projeto = projeto

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if not valor:
            raise ValueError("Código não pode ser vazio ou nulo")
        self._codigo = valor

    @property
    def data_inicio(self):
        return self._data_inicio

    @data_inicio.setter
    def data_inicio(self, valor):
        if not valor:
            raise ValueError("Data de início não pode ser vazia ou nula")
        self._data_inicio = valor

    @property
    def data_fim(self):
        return self._data_fim

    @data_fim.setter
    def data_fim(self, valor):
        if not valor:
            raise ValueError("Data de fim não pode ser vazia ou nula")
        self._data_fim = valor

    @property
    def aluno(self):
        return self._aluno

    @aluno.setter
    def aluno(self, valor):
        if valor is None:
            raise ValueError("Aluno não pode ser nulo")
        self._aluno = valor

    @property
    def projeto(self):
        return self._projeto

    @projeto.setter
    def projeto(self, valor):
        if valor is None:
            raise ValueError("Projeto não pode ser nulo")
        self._projeto = valor

    def __str__(self):
        return (
            f'Participacao[codigo={self.codigo}, '
            f'data_inicio={self.data_inicio}, '
            f'data_fim={self.data_fim}, '
            f'aluno={self.aluno.prontuario}, '
            f'projeto={self.projeto.codigo}]'
        )
