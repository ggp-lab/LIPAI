'''Exercicio 1'''

import pandas as pd


dados = pd.read_csv('src/08-machine-learning/exercicios/wine.csv')


colunas_numericas = dados.select_dtypes(include='number').columns


colunas_numericas = [col for col in colunas_numericas if col != 'Class']


for atributo in colunas_numericas:
    media = dados[atributo].mean()
    mediana = dados[atributo].median()
    desvio_padrao = dados[atributo].std()
    variancia = dados[atributo].var()
    minimo = dados[atributo].min()
    maximo = dados[atributo].max()

    print(f'\nAtributo: {atributo}')
    print(f'Média: {media:.2f}')
    print(f'Mediana: {mediana:.2f}')
    print(f'Desvio padrão: {desvio_padrao:.2f}')
    print(f'Variância: {variancia:.2f}')
    print(f'Mínimo: {minimo:.2f}')
    print(f'Máximo: {maximo:.2f}')
