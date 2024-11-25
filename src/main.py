import textos as txt
from partida import Partida
from utility import *

class Jogo:

    def __init__(self):
        print(txt.intro)
        self.mostrar_opcoes()


    def mostrar_opcoes(self):
        print(txt.opcoes)
        opcoes_validas = ['i', 'c', 'p', 's']
        opcao = input_da_lista("Digite a opção desejada: ", opcoes_validas)

        if opcao == 'i':
            nome = input("Digite o nome do jogador: ")
            linhas = input_int("Digite o número de linhas da tela do jogo: ")
            colunas = input_int("Digite o número de colunas da tela do jogo: ")

            partida = Partida(nome, linhas, colunas)


if __name__ == "__main__":
    jogo = Jogo()