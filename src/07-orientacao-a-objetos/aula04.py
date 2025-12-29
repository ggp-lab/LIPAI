"""Aula 04 - Propriedades"""

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura


    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, value):
        if value <= 0.0:
            raise ValueError("A base deve ser maior que zero")
        self._base = value

    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, value):
        if value <= 0.0:
            raise ValueError("A base deve ser maior que zero")
        self._altura = value

    @classmethod
    def from_list(cls, lista):
        return cls(lista[0], lista[1])
    
    @classmethod
    def from_string(cls, rep_retangulo):
        base, altura = rep_retangulo.split(sep=',')
        return cls(float(base), float(altura))
    
    def calcular_area(self):
        return self.base * self.altura
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

retangulo1 = Retangulo(10.0, 5.0)

retangulo1.base = 30.0
retangulo1.altura = 30.0
print(retangulo1.base)





















