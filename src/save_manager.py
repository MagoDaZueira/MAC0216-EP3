import textos as txt
from utility import *
import pickle
import os


def salvar_partida(partida):
    data = data_atual()
    path = cria_diretorio('saves')
    path = os.path.join(path, f'{partida.nome}_{data}.pkl')
    with open(path, 'wb') as arquivo:
        pickle.dump(partida, arquivo)
    print(txt.texto_ao_salvar)


def mostrar_saves():
    path = cria_diretorio('saves')
    itens = os.listdir(path)

    arquivos = [item for item in itens if os.path.isfile(os.path.join(path, item))]

    print("Escolha o seu save, não desista:")
    for i, arquivo in enumerate(arquivos, start=1):
        print(f'{i}) {arquivo[:-4]}')
        
    while True:
        i = input_int("Digite o número do save desejado: ", 1, len(arquivos))
        return arquivos[i-1][:-4]