from peca import Peca
from math import ceil
from readchar import readkey, key
import os

class Partida:
    
    def __init__(self, nome, linhas, colunas):
        self.nome = nome
        self.linhas = linhas
        self.colunas = colunas

        # Desenha o layout inicial
        self.grid_fixo = self.preparar_grid()
        self.grid_draw = [row[:] for row in self.grid_fixo] # Copia grid_fixo

        # Cria uma peça e a seleciona como atual
        self.peca_ativa: Peca = Peca.gerar_peca_aleatoria(ceil(colunas / 2))

        self.desenhar_peca()
        self.mostrar_tela()

        self.executar_jogo()


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
        grid[0][0]                = ' '
        grid[self.linhas+1][0]         = ' '
        grid[0][self.colunas+1]        = ' '
        grid[self.linhas+1][self.colunas+1] = ' '

        return grid


    def mostrar_tela(self):
        """Imprime os elementos presentes no jogo,
        baseado na matriz self.grid_draw"""
        # os.system('cls||clear')
        for linha in self.grid_draw:
            for caractere in linha:
                print(caractere, end=" ")
            print()

    def desenhar_peca(self):
        # Limpa a peça anterior
        self.grid_draw = [row[:] for row in self.grid_fixo]
        for bloco in self.peca_ativa.blocos:
            x = round(self.peca_ativa.x + bloco[0])
            y = round(self.peca_ativa.y + bloco[1])
            self.grid_draw[y][x] = self.peca_ativa.caractere
            
    
    def executar_jogo(self):
        valores = {"a": (-1, 0), "d": (1, 0), "s": (0, 1)}
        teclas = valores.keys()
        while True:
            tecla = readkey()
            if tecla in teclas:
                os.system('cls||clear')
                self.peca_ativa.mover(valores[tecla][0], valores[tecla][1], self.grid_fixo)

                self.desenhar_peca()
                self.mostrar_tela()


            