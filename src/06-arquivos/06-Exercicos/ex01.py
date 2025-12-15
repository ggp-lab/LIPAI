"""Exercicio 01"""

def carregar_dados_alunos(dados):


    lista_final = []

    with open(dados, 'r') as arq:
        for linha in arq:
            
            linha = linha.strip()
            linha = linha.split(',')


            aluno = {

                'prontuario': linha[0],
                'nome': linha[1],
                'email': linha[2]

            }
            lista_final.append(aluno)
        
    return tuple(lista_final)

    
















