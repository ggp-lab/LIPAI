"""Exemplos das Aulas"""

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

x_trig = np.linspace(0, 2 * np.pi, 100) 
x_int = np.arange(0, 10, 0.1)           


fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))


axs[0, 0].plot(x_trig, np.cos(x_trig), color='blue', linewidth=2)
axs[0, 0].set_title('Gráfico básico (Cosseno)')
axs[0, 0].set_xlabel('Tempo (s)')
axs[0, 0].set_ylabel('Amplitude')



axs[0, 1].plot(x_trig, np.cos(x_trig), label='Cosseno', linestyle='--')
axs[0, 1].plot(x_trig, np.sin(x_trig), label='Seno', color='red')
axs[0, 1].set_title('Seno e cosseno sobrepostos')
axs[0, 1].legend() 



y_quad = x_int ** 2
axs[1, 0].plot(x_int, y_quad, color='green')
axs[1, 0].set_title('Marcadores e linhas paralelas')


axs[1, 0].plot(5, 25, marker='o', color='black', markersize=8) 

axs[1, 0].axhline(25, color='gray', linestyle=':', xmax=0.5) 
axs[1, 0].axvline(5, color='gray', linestyle=':', ymax=0.25) 



axs[1, 1].plot(x_int, np.exp(x_int / 3), color='purple')
axs[1, 1].set_title('Inserindo texto customizado')


axs[1, 1].text(2, 10, 'Curva exponencial\ncresce rápido!', fontsize=10, color='black',
               bbox=dict(facecolor='white', alpha=0.7)) 



plt.suptitle('Curso Matplotlib', fontsize=16, fontweight='bold')


plt.tight_layout() 
plt.subplots_adjust(top=0.90) 

plt.show()