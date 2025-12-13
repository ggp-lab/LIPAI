"""Aula 03 - Exemplos Artigo"""


def titulos_mundiais(pais, *args):
    print('País:', pais)
    for titulos in args:
        print('Ano: ', titulos)


titulos_mundiais('Brasil', '1958', '1962', '1970', '1994', '2002')

titulos_mundiais('Espanha', '2010')


def calcular_preco(valor, **kwargs):
    imposto = kwargs.get('imposto')
    disconto = kwargs.get('disconto')
    if imposto:
        valor += valor * (imposto / 100)
    if disconto:
        valor -= disconto
    return valor


preco_final = calcular_preco(100.0)
print(preco_final)

preco_final = calcular_preco(100.0, disconto=0.5)
print(preco_final)

preco_final = calcular_preco(100.0, imposto=7)
print(preco_final)

preco_final = calcular_preco(100.0, imposto=7, disconto=5.0)
print(preco_final)