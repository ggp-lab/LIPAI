'''Exercicio 6'''

import pandas as pd
import matplotlib.pyplot as plt

base = pd.read_csv('src/08-machine-learning/exercicios/wine.csv')

atributos = [col for col in base.columns if col != 'Class']
percentuais = [0.10, 0.30, 0.50]

amostras = []
for percentual in percentuais:
    subconjunto = base.sample(frac=percentual, random_state=42)
    amostras.append((f'{int(percentual * 100)}%', subconjunto))

amostras.append(('100%', base.copy()))

estatisticas = {}
for nome_amostra, tabela in amostras:
    estatisticas[nome_amostra] = tabela[atributos].describe().loc[['mean', '50%', 'std', 'min', 'max']]

nomes_metricas = {
    'mean': 'Média',
    '50%': 'Mediana',
    'std': 'Desvio padrão',
    'min': 'Mínimo',
    'max': 'Máximo'
}

for codigo_metrica, titulo_metrica in nomes_metricas.items():
    fig, axes = plt.subplots(3, 5, figsize=(16, 9))
    axes = axes.flatten()

    for indice, atributo in enumerate(atributos):
        valores = [estatisticas[nome].loc[codigo_metrica, atributo] for nome, _ in amostras]
        rotulos = [nome for nome, _ in amostras]

        axes[indice].bar(rotulos, valores)
        axes[indice].set_title(atributo, fontsize=9)
        axes[indice].tick_params(axis='x', labelrotation=45)

    for indice in range(len(atributos), len(axes)):
        axes[indice].set_visible(False)

    fig.suptitle(f'Comparação da {titulo_metrica} por tamanho de amostra')
    plt.tight_layout()
    plt.show()

# Conforme o tamanho da amostra aumenta, as métricas estatísticas tendem a ficar mais próximas
# das métricas da base completa. Isso mostra que amostras maiores representam melhor o conjunto de dados.