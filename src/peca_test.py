from partida import Partida
from peca import PecaO, PecaL
from math import ceil

class TestPeca:
    def test_mover(self):
        resultado_esperado = [[' ', '_', '_', '_', ' '], 
                            ['|', '@', '@', ' ', '|'], 
                            ['|', '@', '@', ' ', '|'], 
                            ['|', ' ', ' ', ' ', '|'],
                            [' ', '_', '_', '_', ' ']]
        
        partida = Partida("jogador", 3, 3)
        partida.peca_ativa = PecaO(ceil(3/2))
        partida.peca_ativa.mover(-1, 0, partida.grid_fixo)
        partida.desenhar_peca()
        grid_final = partida.grid_draw
        
        assert grid_final == resultado_esperado

    def test_rotacionar_peca_esquerda(self):
        partida = Partida('jogador', 3, 3)
        partida.peca_ativa = PecaL(ceil(3 / 2))
        partida.peca_ativa.rotacionar_esquerda(partida.grid_fixo)
        partida.desenhar_peca()

        resultado_esperado = [[' ', '_', '_', '_', ' '], 
                                ['|', '&', '&', ' ', '|'], 
                                ['|', ' ', '&', ' ', '|'], 
                                ['|', ' ', '&', ' ', '|'],
                                [' ', '_', '_', '_', ' ']]

        assert resultado_esperado == partida.grid_draw

    def test_rotacionar_peca_direita(self):
        partida = Partida('jogador', 3, 3)
        partida.peca_ativa = PecaL(ceil(3 / 2))
        partida.peca_ativa.rotacionar_direita(partida.grid_fixo)
        partida.desenhar_peca()

        resultado_esperado = [[' ', '_', '_', '_', ' '], 
                                ['|', ' ', '&', ' ', '|'], 
                                ['|', ' ', '&', ' ', '|'], 
                                ['|', ' ', '&', '&', '|'],
                                [' ', '_', '_', '_', ' ']]

        assert resultado_esperado == partida.grid_draw