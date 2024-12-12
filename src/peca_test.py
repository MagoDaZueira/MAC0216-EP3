##
# \file peca_test.py
# \brief Implementação da classe TestPeca.
##

from partida import Partida
from peca import PecaO, PecaL
from math import ceil

##
# \class TestPeca
# \brief Contém atributos e métodos destinados a testar métodos da classe Peca

# \details Estão incluídos testes para os métodos:
#          mover, rotacionar_peca_esquerda e
#          rotacionar_peca_direita
##
class TestPeca:
    ##
    # \brief Testa o movimento da peça ativa.
    #
    # Este teste verifica se a peça pode se mover corretamente para a esquerda no grid.
    # O resultado esperado é que a peça se mova uma posição à esquerda, sem causar colisões.
    # 
    # \return Não retorna valores. Realiza uma asserção sobre o grid final.
    ##
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

    ##
    # \brief Testa a rotação da peça para a esquerda.
    #
    # Este teste verifica se a peça do tipo PecaL consegue rotacionar corretamente
    # para a esquerda no grid. A rotação deve ser aplicada levando em consideração
    # as posições dos blocos e as restrições do grid.
    #
    # \return Não retorna valores. Realiza uma asserção sobre o grid final após rotação.
    ##
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

    ##
    # \brief Testa a rotação da peça para a direita.
    #
    # Este teste verifica se a peça do tipo PecaL consegue rotacionar corretamente
    # para a direita no grid. A rotação deve ser aplicada levando em consideração
    # as posições dos blocos e as restrições do grid.
    #
    # \return Não retorna valores. Realiza uma asserção sobre o grid final após rotação.
    ##
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