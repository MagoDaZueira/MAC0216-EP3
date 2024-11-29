import textos as txt
from partida import Partida
from readchar import readkey, key
from utility import *
import sys
import os
import pickle

class Jogo:

    def __init__(self):
        print(txt.intro)
        self.mostrar_opcoes()
        self.partida_ativa = None


    def mostrar_opcoes(self):
        print(txt.menu_principal)
        opcoes_validas = ['i', 'c', 'p', 's']
        opcao = input_da_lista("Digite a opção desejada: ", opcoes_validas)

        if opcao == 'i':
            nome = input("Digite o nome do jogador: ")
            linhas = input_int("Digite o número de linhas da tela do jogo: ")
            colunas = input_int("Digite o número de colunas da tela do jogo: ")

            # Inicia a partida
            self.partida_ativa = Partida(nome, linhas, colunas)
            self.executar_jogo()
        
        elif opcao == 's':
            self.sair()

        elif opcao == 'c':
            save_escolhido = self.mostrar_saves()
            with open(f"./saves/{save_escolhido}.pkl", "rb") as arquivo:
                self.partida_ativa = pickle.load(arquivo)
            self.executar_jogo()


    def mostrar_saves(self):
        itens = os.listdir('./saves')

        arquivos = [item for item in itens if os.path.isfile(os.path.join('./saves', item))]

        print("Escolha o seu save, não desista:")
        for i, arquivo in enumerate(arquivos, start=1):
            print(f'{i}) {arquivo[:-4]}')
        
        while True:
            i = int(input("Digite o nome do save desejado: "))
            if  i <= len(arquivos):
                return arquivos[i-1][:-4]
            else:
                print('Esse save não existe não, tente novamente')

    
    def executar_jogo(self):
        """Contém o loop principal do jogo."""

        # Mostra a tela ao iniciar o jogo
        self.partida_ativa.mostrar_tela()

        # Direções de cada uma das teclas de movimento
        valores_mov = {"a": (-1, 0), "d": (1, 0), "s": (0, 1)}
        teclas_mov = valores_mov.keys()

        while True:
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

            elif tecla == 'k':
                self.sair()
            elif tecla == 'g':
                os.makedirs('./saves', exist_ok=True)
                data = data_atual()
                with open(f'./saves/{self.partida_ativa.nome}_{data}.pkl', 'wb') as arquivo:
                    pickle.dump(self.partida_ativa, arquivo)
                print(txt.texto_ao_salvar)
                sys.exit()


    
    def sair(self):
        print(txt.despedida)
        sys.exit()


if __name__ == "__main__":
    jogo = Jogo()