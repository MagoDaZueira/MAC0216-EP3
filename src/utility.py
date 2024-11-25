"""@package docstring
Módulo utilitário
 
Contém algumas funções genéricas que auxiliam o resto do programa.
"""


def input_int(prompt: str) -> int:
    """Função que pede um input até que o usuário digite um inteiro.

    - Parâmetro:
    - - prompt - Mensagem que pede input ao usuário

    Retorna um inteiro, o último valor digitado pelo usuário"""

    while True:
        valor = input(prompt)
        try:
            # Tenta converter para inteiro
            return int(valor)
        except ValueError:
            # Caso não seja um número
            print("Valor inválido. Digite um número inteiro.")


def input_da_lista(prompt: str, lista: list) -> any:
    """Função que pede um input até que o usuário digite um valor válido.

    - Parâmetros:
    - - prompt - mensagem que pede input ao usuário
    - - lista - contém os valores válidos

    Retorna o último valor válido digitado pelo usuário"""

    while True:
        valor = input(prompt)
        if valor in lista:
            return valor
        else:
            print("Valor inválido. Tente novamente.")