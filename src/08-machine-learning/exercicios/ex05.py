'''Exercicio 5'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
    preenchido_media[coluna] = preenchido_media[coluna].fillna(base[coluna].mean())
    preenchido_mediana[coluna] = preenchido_mediana[coluna].fillna(base[coluna].median())
    preenchido_moda[coluna] = preenchido_moda[coluna].fillna(base[coluna].mode()[0])

fig, axes = plt.subplots(3, 5, figsize=(16, 9))
axes = axes.flatten()

for i, coluna in enumerate(colunas_numericas):
    conjuntos = [
        base[coluna].dropna(),
        preenchido_media[coluna].dropna(),
        preenchido_mediana[coluna].dropna(),
        preenchido_moda[coluna].dropna()
    ]

    axes[i].boxplot(conjuntos, labels=['Orig', 'Média', 'Mediana', 'Moda'])
    axes[i].set_title(coluna)

for i in range(len(colunas_numericas), len(axes)):
    axes[i].set_visible(False)

plt.tight_layout()
plt.show()

# O boxplot permite comparar a distribuição dos atributos antes e após a imputação.
# Alguns atributos são mais simétricos, enquanto outros apresentam assimetria e outliers.