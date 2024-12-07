import io
import sys
import os
from utility import *

class TestUtility:
    
    def test_input_int(self):
        prompt = "Texto para o teste"
        input_int(prompt=prompt, low=2, up=6)

    def test_cria_diretorio(self):
        cria_diretorio('meu_diretorio_do_ep3')
        diretorio_criado = os.path.isdir('meu_diretorio_do_ep3')
        os.remove("meu_diretorio_do_ep3")
        
        assert diretorio_criado == True

