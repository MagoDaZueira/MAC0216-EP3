import io
import sys
from partida import *
from peca import PecaL

#class TestPartida:

def test_preparar_grid():
    partida = Partida('jogador', 3, 3)
    grid = partida.preparar_grid()
    resultado_esperado = [[' ', '_', '_', '_', ' '], 
                          ['|', ' ', ' ', ' ', '|'], 
                          ['|', ' ', ' ', ' ', '|'], 
                          ['|', ' ', ' ', ' ', '|'],
                          [' ', '_', '_', '_', ' ']]
    
    assert grid == resultado_esperado

def test_mostrar_tela():
    partida = Partida('jogador', 3, 3)
    partida.peca_ativa = PecaL(ceil(3 / 2))

    buffer = io.StringIO()
    sys.stdout = buffer

    partida.mostrar_tela()

    sys.stdout = sys.__stdout__

    resultado_esperado = """  _ _ _   
|     & | 
| & & & | 
|       | 
  _ _ _   

Pontuação: 0
Teclas do jogo:
<a> move esquerda | <d> move direita | <s> move baixo
← rotaciona esquerda | → rotaciona direita
<k> sai da partida, <g> grava e sai da partida
"""

    assert resultado_esperado == buffer.getvalue()



