"""Exercicio 02"""

def carregar_dados_projetos(dados):

    lista_final = []

    with open(dados, 'r') as arq:
        for linha in arq:

            linha = linha.strip()
            linha = linha.split(',')

            projeto = {

                'codigo': (int(linha[0])),
                'titulo': linha[1],
                'responsavel': linha[2]


            }
            lista_final.append(projeto)
    return tuple(lista_final)
     









