'''Exercicio 2'''

import pandas as pd
import matplotlib.pyplot as plt


dados = pd.read_csv('src/08-machine-learning/exercicios/wine.csv')


atributos = dados.select_dtypes(include='number').columns
atributos = [coluna for coluna in atributos if coluna != 'Class']


figura, axes = plt.subplots(3, 5, figsize=(15, 8))
axes = axes.flatten()


for i, coluna in enumerate(atributos):
    axes[i].hist(dados[coluna], bins=10, edgecolor='black')
    axes[i].set_title(coluna)
    axes[i].set_xlabel('Valores')
    axes[i].set_ylabel('Frequência')


for j in range(len(atributos), len(axes)):
    axes[j].set_visible(False)

plt.tight_layout()
plt.show()