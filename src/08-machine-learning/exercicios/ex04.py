'''Exercicio 4'''

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

def mostrar_histogramas(tabela, titulo):
    fig, axes = plt.subplots(3, 5, figsize=(15, 8))
    axes = axes.flatten()

    for i, atributo in enumerate(colunas_numericas):
        axes[i].hist(tabela[atributo], bins=10, edgecolor='black')
        axes[i].set_title(atributo)

    for i in range(len(colunas_numericas), len(axes)):
        axes[i].set_visible(False)

    fig.suptitle(titulo)
    plt.tight_layout()
    plt.show()

mostrar_histogramas(preenchido_media, 'Histogramas após imputação pela média')
mostrar_histogramas(preenchido_mediana, 'Histogramas após imputação pela mediana')
mostrar_histogramas(preenchido_moda, 'Histogramas após imputação pela moda')