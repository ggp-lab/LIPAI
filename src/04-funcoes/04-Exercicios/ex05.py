"""Exercicio 05"""


altura_A0 = input('Qual é sua Altura (m): ', )
peso_P0 = input('Qual seu peso (kg): ')

altura = float(altura_A0)
peso = float(peso_P0)

individuo = {
    'altura': altura,
    'peso': peso

}

def calcular_imc(individuo):
    altura = individuo['altura']
    peso = individuo['peso']

    imc = peso / (altura * altura)
    return imc


def obter_classificacao(imc):
    if 18.5 <= imc <= 24.9:
        return 'Peso Normal'
    elif 25.0 <= imc <= 29.9:
        return 'Excesso de peso'
    elif 30.0 <= imc <= 34.9:
        return 'Obesidade de Classe 1'
    elif 35.0 <= imc <= 39.9:
        return 'Obesidade de Classe 2'
    elif imc >= 40.0:
        return 'Obesidade de Classe 3'
    elif imc < 18.5:
        return 'Abaixo do Peso'

def situacao_individuo(imc):
    classificacao = obter_classificacao(imc)
    if  classificacao == 'Peso Normal':
        return 'Normal'
    elif classificacao in ['Excesso de peso', 'Obesidade de Classe 1', 'Obesidade de Classe 2', 'Obesidade de Classe 3']:
        return 'Perder Peso'
    elif classificacao == 'Abaixo do Peso':
        return 'Ganhar Peso'


imc = calcular_imc(individuo)
classificacao = obter_classificacao(imc)
situacao = situacao_individuo(imc)



print('O IMC do paciente é: ', imc)
print('Sua Classificacao é: ', classificacao)
print('Sua situacao é: ', situacao)
