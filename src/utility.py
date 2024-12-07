##
# \file utility.py
# \brief Contém funções genéricas que auxiliam o resto do programa.
##

from datetime import datetime
import os

##
# \brief Função que pede um input até que o usuário digite um inteiro dentro dos limites especificados.
#
# \param prompt Mensagem que pede input ao usuário.
# \param low Limite inferior para o número. None por padrão.
# \param up Limite superior para o número. None por padrão.
#
# \return Retorna um inteiro, o último valor digitado pelo usuário.
##
def input_int(prompt: str, low: int = None, up: int = None) -> int:
    while True:
        valor = input(prompt)
        valido = True

        try:
            # Tenta converter para inteiro
            valor = int(valor)

            # Verifica se está nos limites
            if low != None:
                if valor < low:
                    valido = False
            if up != None:
                if valor > up:
                    valido = False

            if valido:
                return valor
            else:
                if low == None:
                    print(f'Valor inválido. Digite um número até {up}.')
                elif up == None:
                    print(f'Valor inválido. Digite um número a partir de {low}.')
                else:
                    print(f'Valor inválido. Digite um número entre {low} e {up}.')

        except ValueError:
            # Caso não seja um número
            print("Valor inválido. Digite um número inteiro.")

##
# \brief Função que pede um input até que o usuário digite um valor válido.
#
# \param prompt Mensagem que pede input ao usuário.
# \param lista Contém os valores válidos.
#
# \return Retorna o último valor válido digitado pelo usuário.
##
def input_da_lista(prompt: str, lista: list) -> any:
    while True:
        valor = input(prompt)
        if valor in lista:
            return valor
        else:
            print("Valor inválido. Tente novamente.")

##
# \brief Recolhe a data atual e a formata adequadamente.
# \return A data atual, num formato específico, em string.
##
def data_atual() -> str:
    data = datetime.now()

    # Formatar a data e hora no formato desejado
    return data.strftime("%d-%m-%Y_%Hh%Mm%Ss")

##
# \brief Cria um novo diretório no caminho onde o script está localizado,
#        caso não exista um de mesmo nome.
#
# \param dirname Nome do diretório a ser criado.
#
# \return Retorna o caminho absoluto do diretório criado.
##
def cria_diretorio(dirname: str) -> str:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    novo_diretorio = os.path.join(script_dir, dirname)
    os.makedirs(novo_diretorio, exist_ok=True)

    return novo_diretorio
