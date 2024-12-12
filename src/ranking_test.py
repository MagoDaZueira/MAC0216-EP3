##
# \file ranking_test.py
# \brief Implementação dos testes para o gerenciamento do ranking.
##

import os
import sys
import io
from ranking_manager import *

##
# \class TestRanking
# \brief Contém testes destinados a validar o funcionamento do sistema de ranking.
# 
# \details Este teste verifica se o método de atualização do ranking está funcionando corretamente.
#          O método `atualizar_ranking` é chamado com diferentes jogadores e pontuações e verifica-se
#          se o arquivo de ranking é atualizado corretamente.
##
class TestRanking:

    ##
    # \brief Testa o método atualizar_ranking
    #
    # \return Não retorna valores. Realiza uma asserção sobre o conteúdo do arquivo de ranking.
    ##
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

    

