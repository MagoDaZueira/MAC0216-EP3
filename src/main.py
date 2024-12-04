##
# \file main.py
# \brief Implementação da classe Jogo, e portanto
#        do loop de gameplay principal.
##

import textos as txt
from partida import Partida
from readchar import readkey, key
from utility import *
import ranking_manager as rank
import save_manager as save
import sys
import os
import pickle

##
# \class Jogo
# \brief Atributos e métodos relativos ao loop principal do jogo
#
# \details Seus métodos incluem mostrar o menu principal
#          e executar uma partida. Em ambas situações, é
#          recolhido o input do jogador.
#          Guarda a partida ativa num atributo.
#
# Os métodos envolvem a movimentação e rotação da peça,
# além da criação de novas peças.
##
class Jogo:

    ##
    # \brief Construtor da classe Jogo
    ##
    def __init__(self):
        print(txt.intro)
        self.partida_ativa = None

    ##
    # \brief Mostra o menu principal do jogo, e chama funções que
    #        realizem o solicitado (iniciar, sair, ranking ou carregar).
    #
    # \return Não retorna valores.
    ##
    def mostrar_opcoes(self) -> None:
        print(txt.menu_principal)
        opcoes_validas = ['i', 'c', 'p', 's']
        opcao = input_da_lista("Digite a opção desejada: ", opcoes_validas)

        if opcao == 'i':
            nome = input("Digite o nome do jogador: ")
            linhas = input_int("Digite o número de linhas da tela do jogo: ")
            colunas = input_int("Digite o número de colunas da tela do jogo: ")

            # Inicia a partida
            self.partida_ativa = Partida(nome, linhas, colunas)
            self.executar_partida()
            
        elif opcao == 's':
            self.sair()

        elif opcao == 'c':
            save_escolhido = save.mostrar_saves()
            path = cria_diretorio('saves')
            path = os.path.join(path, f'{save_escolhido}.pkl')
            with open(path, "rb") as arquivo:
                self.partida_ativa = pickle.load(arquivo)
            self.executar_partida()

        elif opcao == 'p':
            rank.mostrar_ranking()
                

    ##
    # \brief Contém o loop principal da partida.
    #
    # \return Não retorna valores.
    ##
    def executar_partida(self):

        # Mostra a tela ao iniciar o jogo
        self.partida_ativa.mostrar_tela()

        # Direções de cada uma das teclas de movimento
        valores_mov = {"a": (-1, 0), "d": (1, 0), "s": (0, 1)}
        teclas_mov = valores_mov.keys()

        while not self.partida_ativa.game_over:
            tecla = readkey() # Input do jogador
            
            # Movimento para esquerda, direita ou baixo
            if tecla in teclas_mov:
                self.partida_ativa.mover_peca(valores_mov[tecla])
            
            # Rotação para a esquerda
            elif tecla == key.LEFT:
                self.partida_ativa.rotacionar_peca_esquerda()

            # Rotação para a direita
            elif tecla == key.RIGHT:
                self.partida_ativa.rotacionar_peca_direita()

            # Sair sem salvar
            elif tecla == 'k':
                break
            
            # Sair salvando
            elif tecla == 'g':
                save.salvar_partida(self.partida_ativa)
                break
        
        # Caso a partida tenha acabado, atualiza ranking
        if self.partida_ativa.game_over:
            rank.atualizar_ranking(self.partida_ativa.nome, self.partida_ativa.pontuacao)
            
    ##
    # \brief Finaliza o programa.
    #
    # \return Não retorna valores.
    ##
    def sair(self):
        print(txt.despedida)
        sys.exit()


# Executado ao rodar o script
if __name__ == "__main__":

    # Inicia o jogo
    jogo = Jogo()

    # Quando alguma funcionalidade termina, mostra menu novamente
    while True:
        jogo.mostrar_opcoes()