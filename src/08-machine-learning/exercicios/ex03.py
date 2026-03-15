'''exercicio 3'''

import pandas as pd
import numpy as np

base = pd.read_csv('src/08-machine-learning/exercicios/wine.csv')

dados_com_falhas = base.copy()
gerador = np.random.default_rng(42)
percentual_nulos = 0.10

colunas_numericas = [col for col in dados_com_falhas.columns if col != 'Class']

for coluna in colunas_numericas:
    linhas_sorteadas = gerador.choice(
        dados_com_falhas.index,
        size=int(len(dados_com_falhas) * percentual_nulos),
        replace=False
    )
    dados_com_falhas.loc[linhas_sorteadas, coluna] = np.nan

preenchido_media = dados_com_falhas.copy()
preenchido_mediana = dados_com_falhas.copy()
preenchido_moda = dados_com_falhas.copy()

for coluna in colunas_numericas:
    valor_media = base[coluna].mean()
    valor_mediana = base[coluna].median()
    valor_moda = base[coluna].mode()[0]

    preenchido_media[coluna] = preenchido_media[coluna].fillna(valor_media)
    preenchido_mediana[coluna] = preenchido_mediana[coluna].fillna(valor_mediana)
    preenchido_moda[coluna] = preenchido_moda[coluna].fillna(valor_moda)

print('Valores ausentes antes do preenchimento:')
print(dados_com_falhas.isna().sum())

print('\nValores ausentes após preenchimento pela média:')
print(preenchido_media.isna().sum())

print('\nValores ausentes após preenchimento pela mediana:')
print(preenchido_mediana.isna().sum())

print('\nValores ausentes após preenchimento pela moda:')
print(preenchido_moda.isna().sum())