import textos as txt
from utility import *
import pickle
import os


def salvar_partida(partida):
    os.makedirs('./saves', exist_ok=True)
    data = data_atual()
    with open(f'./saves/{partida.nome}_{data}.pkl', 'wb') as arquivo:
        pickle.dump(partida, arquivo)
    print(txt.texto_ao_salvar)


def mostrar_saves():
    itens = os.listdir('./saves')

    arquivos = [item for item in itens if os.path.isfile(os.path.join('./saves', item))]

    print("Escolha o seu save, não desista:")
    for i, arquivo in enumerate(arquivos, start=1):
        print(f'{i}) {arquivo[:-4]}')
        
    while True:
        i = input_int("Digite o número do save desejado: ", 1, len(arquivos))
        return arquivos[i-1][:-4]