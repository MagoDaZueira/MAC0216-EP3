import io
import sys
from partida import *
from peca import PecaL, Peca

class TestPartida:

    def test_preparar_grid(self):
        partida = Partida('jogador', 3, 3)
        grid = partida.preparar_grid()
        resultado_esperado = [[' ', '_', '_', '_', ' '], 
                            ['|', ' ', ' ', ' ', '|'], 
                            ['|', ' ', ' ', ' ', '|'], 
                            ['|', ' ', ' ', ' ', '|'],
                            [' ', '_', '_', '_', ' ']]
        
        assert grid == resultado_esperado

    def test_desenhar_peca(self):
        partida = Partida("jogador", 3, 3)
        partida.peca_ativa = PecaL(ceil(3 / 2))

        partida.desenhar_peca()

        grid_draw = partida.grid_draw

        resultado_esperado = [[' ', '_', '_', '_', ' '], 
                            ['|', ' ', ' ', '&', '|'], 
                            ['|', '&', '&', '&', '|'], 
                            ['|', ' ', ' ', ' ', '|'],
                            [' ', '_', '_', '_', ' ']]
        
        assert resultado_esperado[2] == grid_draw[2]

    def test_encaixar_peca(self):
        partida = Partida("jogador", 3, 3)
        partida.peca_ativa = PecaL(ceil(3 / 2))
        partida.desenhar_peca()
        partida.encaixar_peca()

        resultado_esperado = [[' ', '_', '_', '_', ' '],
                             ['|', ' ', ' ', ' ', '|'],
                             ['|', ' ', ' ', '&', '|'],
                             ['|', ' ', ' ', ' ', '|'],
                             [' ', '_', '_', '_', ' ']]
        
        grid_fixo = partida.grid_fixo

        assert resultado_esperado == grid_fixo
            

    def test_linhas_a_limpar(self):
        partida = Partida("jogador", 3, 3)
        partida.grid_fixo = [[' ', '_', '_', '_', ' '], 
                            ['|', ' ', ' ', ' ', '|'], 
                            ['|', ' ', ' ', '&', '|'], 
                            ['|', '&', '&', '&', '|'],
                            [' ', '_', '_', '_', ' ']]
        linhas_completas = partida.linhas_a_limpar([2, 3])
        assert linhas_completas == [3]

    def test_limpar_linhas(self):
        partida = Partida("jogador", 3, 3)
        partida.grid_fixo = [[' ', '_', '_', '_', ' '], 
                            ['|', ' ', ' ', ' ', '|'], 
                            ['|', ' ', ' ', '&', '|'], 
                            ['|', '&', '&', '&', '|'],
                            [' ', '_', '_', '_', ' ']]
        partida.limpar_linhas([3])
        grid_fixo = partida.grid_fixo

        resultado_esperado = [[' ', '_', '_', '_', ' '], 
                            ['|', ' ', ' ', ' ', '|'], 
                            ['|', ' ', ' ', ' ', '|'], 
                            ['|', ' ', ' ', '&', '|'],
                            [' ', '_', '_', '_', ' ']]

        assert resultado_esperado == grid_fixo

    def test_pode_spawnar(self):
        partida = Partida("jogador", 3, 3)
        partida.grid_fixo = [[' ', '_', '_', '_', ' '], 
                            ['|', '@', '@', ' ', '|'], 
                            ['|', '@', '@', '&', '|'], 
                            ['|', '&', '&', '&', '|'],
                            [' ', '_', '_', '_', ' ']]
        partida.peca_ativa = Peca.gerar_peca_aleatoria(ceil(3 / 2))
        pode_spawnar = partida.pode_spawnar()

        assert pode_spawnar == False

test = TestPartida()
test.test_encaixar_peca()    