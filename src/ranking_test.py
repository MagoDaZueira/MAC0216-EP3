import os
import sys
import io
from ranking_manager import *

class TestRanking:

    def test_atualizar_ranking(self): #Assume que o diretorio ranking não existe
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ranking_dir = os.path.join(script_dir, "ranking")
        path = os.path.join(ranking_dir, "ranking.txt")
        conteudo_ranking = ""
        if os.path.isdir(ranking_dir):
            os.remove(path)
            os.rmdir(ranking_dir)

        atualizar_ranking("assembly", 0)
        atualizar_ranking("k", 37)
        atualizar_ranking("a l", 45)
        atualizar_ranking('m', 39)

        with open(path, 'r') as arquivo:
            for linha in arquivo:
                conteudo_ranking = conteudo_ranking + linha

        resultado_esperado = 'a l 45\n' + 'm 39\n' + 'k 37\n' + 'assembly 0\n'

        os.remove(path)
        os.rmdir(ranking_dir)

        assert conteudo_ranking == resultado_esperado

    """def test_mostrar_ranking(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ranking_dir = os.path.join(script_dir, "ranking")
        path = os.path.join(ranking_dir, "ranking.txt")

        if not(os.path.isdir(ranking_dir)):
            os.mkdir(ranking_dir)

        with open(path, 'w') as arquivo:
            arquivo.writelines(['um 10\n', 'dois 6\n', 'tres tres 3\n' ])
        

        buffer = io.StringIO()
        #sys.stdout = buffer
        mostrar_ranking()
        sys.stdout = sys.__stdout__

        resultado_esperado = """"""
    ---------------------------------------------------------
    ----------------- 10 MELHORES PONTUAÇÕES ----------------
    ---------------------------------------------------------

    1) um 10

    2) dois 6

    3) tres tres 3
"""
    """

        os.remove(path)
        os.rmdir(ranking_dir)

        if buffer.getvalue() == resultado_esperado:
            print("igual")"""
    

