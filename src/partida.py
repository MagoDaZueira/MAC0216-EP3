from peca import Peca
from math import ceil
import os
import textos as txt

class Partida:
    
    def __init__(self, nome, linhas, colunas):
        self.nome = nome
        self.linhas = linhas
        self.colunas = colunas

        self.pontuacao = 0
        self.linhas_para_pontuacao = [0, 1, 3, 5, 8]

        # Desenha o layout inicial
        self.grid_fixo = self.preparar_grid()
        self.grid_draw = [row[:] for row in self.grid_fixo] # Copia grid_fixo

        # Cria uma peça e a seleciona como atual
        self.peca_ativa: Peca = Peca.gerar_peca_aleatoria(ceil(colunas / 2))


    def preparar_grid(self):
        """Retorna uma matriz de chars que
        contém o layout básico da tela."""

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


    def mostrar_tela(self):
        """Imprime os elementos presentes no jogo,
        baseado na matriz self.grid_draw"""
        self.desenhar_peca()
        os.system('cls||clear')
        for linha in self.grid_draw:
            for caractere in linha:
                print(caractere, end=" ")
            print()
        
        print(f'\nPontuação: {self.pontuacao}')
        print(txt.menu_ingame)


    def desenhar_peca(self):
        # Limpa a peça anterior
        self.grid_draw = [row[:] for row in self.grid_fixo]
        for bloco in self.peca_ativa.blocos:
            x = round(self.peca_ativa.x + bloco[0])
            y = round(self.peca_ativa.y + bloco[1])
            self.grid_draw[y][x] = self.peca_ativa.caractere
            
    
    def encostou_no_chao(self):
        for bloco in self.peca_ativa.blocos:
            x = round(self.peca_ativa.x + bloco[0])
            y_abaixo = round(self.peca_ativa.y + bloco[1]) + 1

            if self.grid_fixo[y_abaixo][x] != ' ':
                return True
            
        return False
    

    def encaixar_peca(self):
        linhas_com_bloco = []

        for bloco in self.peca_ativa.blocos:
            x = round(self.peca_ativa.x + bloco[0])
            y = round(self.peca_ativa.y + bloco[1])
            self.grid_fixo[y][x] = self.peca_ativa.caractere
            linhas_com_bloco.append(y)

        linhas = self.linhas_a_limpar(set(linhas_com_bloco))
        self.limpar_linhas(linhas)
        self.peca_ativa = Peca.gerar_peca_aleatoria(ceil(self.colunas / 2))

    
    def linhas_a_limpar(self, linhas):
        linhas_finais = []
        for linha in linhas:
            deletavel = True
            for cell in self.grid_fixo[linha]:
                if cell == ' ':
                    deletavel = False
                    break
            if deletavel:
                linhas_finais.append(linha)
        return linhas_finais


    def limpar_linhas(self, linhas: list):
        self.pontuacao += self.linhas_para_pontuacao[len(linhas)]
        linhas.sort()

        for linha in linhas:
            for i in range(linha, 1, -1):
                self.grid_fixo[i] = [j for j in self.grid_fixo[i-1]]

            for j in range(1, len(self.grid_fixo[1]) - 1):
                self.grid_fixo[1][j] = ' '


    def mover_peca(self, direcao: tuple[int]):
        self.peca_ativa.mover(direcao[0], direcao[1], self.grid_fixo)
        self.update()

    def rotacionar_peca_esquerda(self):
        self.peca_ativa.rotacionar_esquerda(self.grid_fixo)
        self.update()

    def rotacionar_peca_direita(self):
        self.peca_ativa.rotacionar_direita(self.grid_fixo)
        self.update()

    def update(self):
        if self.encostou_no_chao():
            self.encaixar_peca()
        self.mostrar_tela()
