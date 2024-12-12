##
# \file partida_teste.py
# \brief Implementação da classe TestPartida.
##

import io
import sys
from partida import *
from peca import PecaL, Peca

##
# \class TestPartida
# \brief Contém atributos e métodos destinados a testar métodos da classe Partida

# \details Estão incluídos testes para os métodos:
#          preparar_grid, desenhar_peca, encaixar_peca,
#          linhas_a_limpar, limpar_linhas e pode_spawnar
##
class TestPartida:

    ##
    # \brief verifica se uma grid 3x3 é corretamente criada
    #
    # \return Não retorna valores.
    ##
    def test_preparar_grid(self):
        partida = Partida('jogador', 3, 3)
        grid = partida.preparar_grid()
        resultado_esperado = [[' ', '_', '_', '_', ' '], 
                            ['|', ' ', ' ', ' ', '|'], 
                            ['|', ' ', ' ', ' ', '|'], 
                            ['|', ' ', ' ', ' ', '|'],
                            [' ', '_', '_', '_', ' ']]
        
        assert grid == resultado_esperado

    ##
    # \brief teste se uma peça é corretamente desenhada no grid_draw
    #
    # \return Não retorna valores.
    ##
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
        
        assert resultado_esperado == grid_draw

    ##
    # \brief testa se a linha completa é apagada 
    #        e se todas as linhas abaixam uma unidade
    #        ao chamar encaixar_peca
    #
    # \return Não retorna valores.
    ##
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
            
    ##
    # \brief testa se a linha completa é identificada
    #        corretamente
    #
    # \return Não retorna valores.
    ##
    def test_linhas_a_limpar(self):
        partida = Partida("jogador", 3, 3)
        partida.grid_fixo = [[' ', '_', '_', '_', ' '], 
                            ['|', ' ', ' ', ' ', '|'], 
                            ['|', ' ', ' ', '&', '|'], 
                            ['|', '&', '&', '&', '|'],
                            [' ', '_', '_', '_', ' ']]
        linhas_completas = partida.linhas_a_limpar([2, 3])
        assert linhas_completas == [3]

    ##
    # \brief testa se a linha pedida é apagada
    #
    # \return Não retorna valores.
    ##
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

    ##
    # \brief testa se identifica corretamente
    #        que não há mais posições para spawnar
    #
    # \return Não retorna valores.
    ##
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
  