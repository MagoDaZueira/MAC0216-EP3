##
# \file ranking_manager.py
# \brief Contém funções de gerenciamento do ranking de pontuações.
##

import os
import textos as txt
from utility import cria_diretorio

def atualizar_ranking(nome: str, pontuacao: int) -> None:
    path = cria_diretorio('ranking')
    path = os.path.join(path, 'ranking.txt')
    if not(os.path.exists(path)):
        with open(path, 'w') as arquivo:
            pass
            
    with open(path, 'r') as arquivo:
        linhas = arquivo.readlines()
        linhas.reverse()
        if len(linhas) < 10:
                linhas.append(f"{nome} {pontuacao}\n")
        else:
            for i, linha in enumerate(linhas[:-1]):
                linha_separada = linha.split()
                if pontuacao > int(linha_separada[-1]):
                    linhas[i] = f"{nome} {pontuacao}\n"
                    break
        
    linhas = sorted(linhas, key=lambda linha: int(linha.strip().split()[-1]), reverse=True)
    with open(path, 'w') as arquivo: 
        arquivo.writelines(linhas)


def mostrar_ranking() -> None:
    path = cria_diretorio('ranking')
    path = os.path.join(path, 'ranking.txt')
    if not(os.path.exists(path)):
        with open(path, 'w') as arquivo:
            pass
    try:
        with open(path, 'r') as arquivo:
            linhas = arquivo.readlines()
            print(txt.ranking)

            i = 1
            for linha in linhas:
                print(f'{i}) {linha}')
                i += 1

    except FileNotFoundError:
        with open(path, 'w') as arquivo:
            print('Ainda não há pontuações registradas, se esforce mais')