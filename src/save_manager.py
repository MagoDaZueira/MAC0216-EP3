##
# \file save_manager.py
# \brief Contém funções relativas ao salvamento do jogo
##

import textos as txt
from utility import *
import pickle
import os

##
# \brief Salva uma partida num .pkl utilizando Pickle
#
# \param partida Objeto a ser salvado,
#                deve ser da classe Partida
#
# \return Não retorna valores.
##
def salvar_partida(partida) -> None:
    data = data_atual()
    path = cria_diretorio('saves')
    path = os.path.join(path, f'{partida.nome}_{data}.pkl')
    with open(path, 'wb') as arquivo:
        pickle.dump(partida, arquivo)
    print(txt.texto_ao_salvar)

##
# \brief Lista as partidas salvas no diretório saves,
#        e permite que o jogador escolha uma delas.
#
# \return Retorna o nome do arquivo selecionado, sem .pkl no fim.
##
def mostrar_saves() -> str:
    path = cria_diretorio('saves')
    itens = os.listdir(path)

    arquivos = [item for item in itens if os.path.isfile(os.path.join(path, item))]

    print("Escolha o seu save, não desista:")
    for i, arquivo in enumerate(arquivos, start=1):
        print(f'{i}) {arquivo[:-4]}')
        
    while True:
        i = input_int("Digite o número do save desejado: ", 1, len(arquivos))
        return arquivos[i-1][:-4]
    
def carregar_partida(arquivo):
    return pickle.load(arquivo)