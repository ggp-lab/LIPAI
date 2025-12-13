"""Exercicio 06"""

comprimento_inicial = input('Qual o comprimento do aquario (cm): ')
largura_inicial = input('Qual a largura do aquario (cm): ')
altura_inicial = input('Qual a altura do aquario (cm): ')
temperatura_desejada_inicial = input('Qual a temperatura desejada do aquario (°C)')
temperatura_ambiente_inicial = input('Qual a temperatura ambiente do aquario (°C)')


comprimento = float(comprimento_inicial)
largura = float(largura_inicial)
altura = float(altura_inicial)
temperatura_ambiente = float(temperatura_ambiente_inicial)
temperatura_desejada = float(temperatura_desejada_inicial)





informacoes = {
    'altura': altura,
    'largura': largura,
    'comprimento': comprimento,
    'temperatura_ambiente': temperatura_ambiente,
    'temperatura_desejada': temperatura_desejada
}

def calcular_volume(informacoes):
    volume = informacoes['altura'] * informacoes['comprimento'] * informacoes['largura'] / 1000
    return volume

volume = calcular_volume(informacoes)


def calcular_termostato(volume, informacoes):
    potencia = volume * 0.05 * (informacoes['temperatura_desejada'] - informacoes['temperatura_ambiente'])
    return potencia


potencia = calcular_termostato(volume, informacoes)

def calcular_filtragem(volume):
    filtragem_min = volume * 2
    filtragem_max = volume * 3

    return filtragem_min, filtragem_max

filtragem_min, filtragem_max = calcular_filtragem(volume)



print('O volume do Aquario é de: ', volume, 'cm^3')
print('-------------------------------------------')
print('A potencia do termostato deve ser de: ', potencia)
print('-------------------------------------------')
print('A filtragem minima deve ser de: ', filtragem_min)
print('-------------------------------------------')
print('A filtragem maxima é de: ', filtragem_max)














