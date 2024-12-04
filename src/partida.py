##
# \file partida.py
# \brief Implementação da classe Partida.
##

from peca import Peca
from math import ceil
import os
import textos as txt

##
# \class Partida
# \brief Contém atributos e métodos relativos a uma partida em específico.

# \details Seus atributos incluem o nome do jogador, número de linhas e
#          colunas, pontuação atual, peça ativa e o estado do grid.
#          Os métodos envolvem a manipulação de atributos como os acima.
##
class Partida:
    
    ##
    # \brief Construtor da classe Partida.
    #
    # \param nome Nome do jogador.
    # \param linhas Quantidade de linhas no grid.
    # \param colunas Quantidade de colunas no grid.
    ##
    def __init__(self, nome, linhas, colunas):
        self.nome = nome
        self.linhas = linhas
        self.colunas = colunas

        self.pontuacao = 0
        self.linhas_para_pontuacao = [0, 1, 3, 5, 8]

        self.rodando = True
        self.game_over = False

        # Desenha o layout inicial
        self.grid_fixo = self.preparar_grid()
        self.grid_draw = [row[:] for row in self.grid_fixo] # Copia grid_fixo

        # Cria uma peça e a seleciona como atual
        self.peca_ativa: Peca = Peca.gerar_peca_aleatoria(ceil(colunas / 2))


    ##
    # \brief Retorna uma matriz de chars que
    #        contém o layout básico da tela.
    #
    # \return Não retorna valores.
    ##
    def preparar_grid(self) -> list[list[str]]:
        grid = [
            [
                '_' if i == 0 or i == self.linhas + 1 else
                '|' if j == 0 or j == self.colunas + 1 else ' '
                for j in range(self.colunas + 2)
            ]
            for i in range(self.linhas + 2)
        ]

        # Bordas arredondadas
        grid[0][0]                          = ' '
        grid[self.linhas+1][0]              = ' '
        grid[0][self.colunas+1]             = ' '
        grid[self.linhas+1][self.colunas+1] = ' '

        return grid

    ##
    # \brief Imprime os elementos presentes no jogo,
    #        baseado na matriz self.grid_draw
    #
    # \return Não retorna valores.
    ##
    def mostrar_tela(self) -> None:
        self.desenhar_peca()
        os.system('cls||clear')
        for linha in self.grid_draw:
            for caractere in linha:
                print(caractere, end=" ")
            print()
        
        print(f'\nPontuação: {self.pontuacao}')
        print(txt.menu_ingame)

    ##
    # \brief Variação de self.mostrar_tela(), imprimindo
    #        informações adicionais relativas ao game over.
    #
    # \return Não retorna valores.
    ##
    def mostrar_gameover(self) -> None:
        self.desenhar_peca()
        os.system('cls||clear')
        for linha in self.grid_draw:
            for caractere in linha:
                print(caractere, end=" ")
            print()

        print(f'Fim da partida!')
        print(f'Pontuação final: {self.pontuacao}')

    ##
    # \brief Com base nos atributos da peça ativa, marca seus
    #        blocos no grid_draw, usado ao mostrar a tela.
    #
    # \return Não retorna valores.
    ##
    def desenhar_peca(self) -> None:
        # Limpa a peça anterior
        self.grid_draw = [row[:] for row in self.grid_fixo]

        # Posição dos blocos da peça
        for bloco in self.peca_ativa.blocos:
            x = round(self.peca_ativa.x + bloco[0])
            y = round(self.peca_ativa.y + bloco[1])
            self.grid_draw[y][x] = self.peca_ativa.caractere
            
    ##
    # \brief Verifica se a peça ativa tocou o chão
    #        (ou outra peça) diretamente abaixo.
    #
    # \return True, se tocou o chão,
    #         e False caso contrário.
    ##
    def encostou_no_chao(self) -> bool:
        for bloco in self.peca_ativa.blocos:
            x = round(self.peca_ativa.x + bloco[0])
            y_abaixo = round(self.peca_ativa.y + bloco[1]) + 1

            if self.grid_fixo[y_abaixo][x] != ' ':
                return True
            
        return False
    
    ##
    # \brief Passa a peça ativa para o grid fixo, encaixando-a.
    #        Depois, chama a rotina de limpar linhas,
    #        caso haja alguma completa.
    #
    # \return Não retorna valores.
    ##
    def encaixar_peca(self) -> None:
        linhas_com_bloco = []

        for bloco in self.peca_ativa.blocos:
            x = round(self.peca_ativa.x + bloco[0])
            y = round(self.peca_ativa.y + bloco[1])
            self.grid_fixo[y][x] = self.peca_ativa.caractere
            linhas_com_bloco.append(y)

        linhas = self.linhas_a_limpar(set(linhas_com_bloco))
        self.limpar_linhas(linhas)
        self.peca_ativa = Peca.gerar_peca_aleatoria(ceil(self.colunas / 2))

    ##
    # \brief Verifica quais linhas estão completas.
    #
    # \param linhas Os índices das linhas possivelmente completas,
    #        especificadas para evitar iterar sobre todo o grid.
    #
    # \return Retorna uma lista com as linhas completas.
    ##
    def linhas_a_limpar(self, linhas) -> list:
        linhas_completas = []
        
        for linha in linhas:
            completa = True
            for cell in self.grid_fixo[linha]:
                if cell == ' ':
                    completa = False
                    break
            if completa:
                linhas_completas.append(linha)

        return linhas_completas

    ##
    # \brief Limpa todas as linhas de uma lista contendo
    #        índices. Depois, desce todas as linhas acima.
    #
    # \param linhas Lista com os índices das linhas a serem limpas.
    #
    # \return Não retorna valores.
    ##
    def limpar_linhas(self, linhas: list) -> None:
        self.pontuacao += self.linhas_para_pontuacao[len(linhas)]
        linhas.sort()

        for linha in linhas:
            for i in range(linha, 1, -1):
                self.grid_fixo[i] = [j for j in self.grid_fixo[i-1]]

            for j in range(1, len(self.grid_fixo[1]) - 1):
                self.grid_fixo[1][j] = ' '


    ##
    # \brief Move a peça ativa na direção especificada.
    #
    # \param direcao Uma tupla de inteiros (dx, dy),
    #                indicando o deslocamento desejado.
    #
    # \return Não retorna valores.
    ##
    def mover_peca(self, direcao: tuple[int]) -> None:
        self.peca_ativa.mover(direcao[0], direcao[1], self.grid_fixo)
        self.update()

    ##
    # \brief Rotaciona a peça ativa para a esquerda.
    # \return Não retorna valores.
    ##
    def rotacionar_peca_esquerda(self) -> None:
        self.peca_ativa.rotacionar_esquerda(self.grid_fixo)
        self.update()

    ##
    # \brief Rotaciona a peça ativa para a direita.
    # \return Não retorna valores.
    ##
    def rotacionar_peca_direita(self) -> None:
        self.peca_ativa.rotacionar_direita(self.grid_fixo)
        self.update()

    ##
    # \brief Chama funções que verificam ou atualizam
    #        o estado da partida.
    #
    # \return Não retorna valores.
    ##
    def update(self) -> None:
        if self.encostou_no_chao():
            self.encaixar_peca()
            if self.pode_spawnar():
                self.mostrar_tela()
            else:
                self.game_over = True
                self.mostrar_gameover()
        else:
            self.mostrar_tela()

    ##
    # \brief Verifica se é possível criar
    #        uma peça nova no grid atual.
    #
    # \return True se é possível,
    #         e False caso contrário.
    ##
    def pode_spawnar(self) -> bool:
        for bloco in self.peca_ativa.blocos:
            x = round(self.peca_ativa.x + bloco[0])
            y = round(self.peca_ativa.y + bloco[1])
            if self.grid_fixo[y][x] != ' ':
                return False
        return True