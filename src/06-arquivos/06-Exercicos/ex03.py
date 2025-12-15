"""Exercicio 03"""

def linha_para_dict(linha, chaves):

    dict_final = {}

    linha = linha.strip()
    linha = linha.split(',')

    tamanho = range(len(linha))

    for i in tamanho:
        dict_final[chaves[i]] = linha[i]


    return dict_final
    
        






