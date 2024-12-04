##
# \file peca.py
# \brief Implementação da classe Peca.
##

import random

##
# \class Peca
# \brief Contém informações e métodos sobre uma peça no jogo.
#
# \details Seus atributos incluem a posição da peça no grid,
#          o caractere a ser utilizado ao desenhá-la, e uma lista
#          de seus blocos componentes.
#
# Os métodos envolvem a movimentação e rotação da peça,
# além da criação de novas peças.
##
class Peca:
    ##
    # \brief Construtor da classe Peca.
    #
    # \param blocos Lista de tuplas contendo as posições (x, y) em relação ao centro da peça.
    # \param x Posição horizontal do centro da peça no grid.
    # \param y Posição vertical do centro da peça no grid.
    # \param caractere Símbolo usado para mostrar esta peça na tela.
    ##
    def __init__(self, blocos: list[tuple], x: int, y: int, caractere: str):

        self.blocos = blocos
        self.x = x
        self.y = y
        self.caractere = caractere

        # Utilizados nos testes ao rotacionar a peça
        self.offsets_rotacao = [(0, 0),
                                (-1, 0), (1, 0),
                                (0, -1), (0, 1),
                                (-1, -1), (1, -1),
                                (-1, 1), (1, 1)]
        
    @staticmethod
    ##
    # \brief Escolhe aleatoriamente um dos possíveis tipos de peças,
    # os quais são subclasses desta classe Peca, e cria essa
    # peça no topo do tabuleiro.
    #    
    # \param centro_x Indica a posição horizontal do grid onde
    #                 a peça deve surgir.
    #
    # \return Um objeto de uma subclasse de Peca
    ##
    def gerar_peca_aleatoria(centro_x: int):


        tipos_de_pecas = [PecaO, PecaI, PecaL, PecaJ, PecaS, PecaZ, PecaT]
        return random.choice(tipos_de_pecas)(centro_x)
    

    ##
    # \brief Move a peça horizontalmente ou para baixo, caso possível.
    #
    # \param dx Deslocamento horizontal desejado.
    # \param dy Deslocamento vertical desejado.
    # \param grid Indica quais posições estão ocupadas e quais livres.
    #             As posições livres devem ser dadas por ' '.
    #
    # \return Não retorna valores.
    ##
    def mover(self, dx: int, dy: int, grid: list[list[str]]) -> None:
        pode_mover = True
        for bloco in self.blocos:
            # Posições dos blocos no grid
            new_x = round(self.x + bloco[0]) + dx
            new_y = round(self.y + bloco[1]) + dy

            if grid[new_y][new_x] != ' ':
                pode_mover = False
            
        if pode_mover:
            self.x += dx
            self.y += dy

    ##
    # \brief Rotaciona a peça para a direita, caso possível.
    #
    # \param grid Indica quais posições estão ocupadas e quais livres.
    #             As posições livres devem ser dadas por ' '.
    #
    # \return Não retorna valores.
    ##
    def rotacionar_direita(self, grid: list[list[str]]) -> None:
        # Lista com novas posições pela fórmula adequada
        novos_blocos = [(-y, x) for (x, y) in self.blocos]

        # Faz os ajustes necessários, caso possíveis
        correcao = self.verificar_rotacao(novos_blocos, grid)

        # Se há algum ajuste válido, atualiza posição dos blocos
        if correcao != None:
            self.blocos = [(x, y) for (x, y) in novos_blocos]
            self.x += correcao[0]
            self.y += correcao[1]


    ##
    # \brief Rotaciona a peça para a esquerda, caso possível.
    #
    # \param grid Indica quais posições estão ocupadas e quais livres.
    #             As posições livres devem ser dadas por ' '.
    #
    # \return Não retorna valores.
    ##
    def rotacionar_esquerda(self, grid: list[list[str]]) -> None:
        # Lista com novas posições pela fórmula adequada
        novos_blocos = [(y, -x) for (x, y) in self.blocos]

        # Faz os ajustes necessários, caso possíveis
        correcao = self.verificar_rotacao(novos_blocos, grid)

        # Se há algum ajuste válido, atualiza posição dos blocos
        if correcao != None:
            self.blocos = [(x, y) for (x, y) in novos_blocos]
            self.x += correcao[0]
            self.y += correcao[1]

    ## 
    # \brief Testa se a rotação é possível, usando uma lista de offsets
    # para verificar se, caso a rotação padrão não seja possível,
    # algum pequeno deslocamento a torna válida.
    #
    # \param posicoes As novas posições relativas dos blocos ao pivô, após a rotação base
    # \param grid Indica quais posições estão ocupadas, e quais livres.
    #               As posições livres devem ser dadas por ' '.
    #
    # \return Uma tupla com um offset que torne a rotação válida, caso possível.
    #         Caso não exista offset válido, retorna None.
    ##
    def verificar_rotacao(self, posicoes: list[tuple], grid: list[list[str]]) -> tuple:

        for offset in self.offsets_rotacao:
            offset_valido = True
            # Novas posições relativas dos blocos, somando offset
            novas_pos = [(pos[0] + offset[0], pos[1] + offset[1]) for pos in posicoes]

            for bloco in novas_pos:
                # Posição dos blocos com offset no grid
                new_x = round(self.x + bloco[0])
                new_y = round(self.y + bloco[1])

                # Fora dos limites da matriz
                if new_x < 0 or new_x >= len(grid[0]) or new_y < 0 or new_y >= len(grid):
                    offset_valido = False
                    break

                # Colisão com algum objeto
                if grid[new_y][new_x] != ' ':
                    offset_valido = False
                    break
            
            if offset_valido:
                return offset
        
        return None


##########################################################
################### SUBCLASSES DE PEÇA ###################
##########################################################

class PecaO(Peca):
    def __init__(self, pos_x):
        super().__init__([  (-0.5, -0.5), (0.5, -0.5),
                            (-0.5, 0.5), (0.5, 0.5)],

                            pos_x + 0.5, 1.5,
                            '@')

class PecaI(Peca):
    def __init__(self, pos_x):
        super().__init__([  (-1.5, -0.5), (-0.5, -0.5), (0.5, -0.5), (1.5, -0.5)],
                         
                            pos_x + 0.5, 1.5,
                            '$')
        
        # A peça I precisa de mais verificações na rotação, muito oblonga
        self.offsets_rotacao.append((-2, 0))
        self.offsets_rotacao.append((2, 0))
        self.offsets_rotacao.append((0, -2))
        self.offsets_rotacao.append((0, 2))
        
class PecaL(Peca):
    def __init__(self, pos_x):
        super().__init__([                   (1, -1),
                            (-1, 0), (0, 0), (1, 0)],

                            pos_x, 2,
                            '&')
        
class PecaJ(Peca):
    def __init__(self, pos_x):
        super().__init__([  (-1, -1),
                            (-1, 0), (0, 0), (1, 0)],

                            pos_x, 2,
                            '#')
        
class PecaS(Peca):
    def __init__(self, pos_x):
        super().__init__([           (0, -1), (1, -1),
                            (-1, 0), (0, 0)],

                            pos_x, 2,
                            '%')
        
class PecaZ(Peca):
    def __init__(self, pos_x):
        super().__init__([  (-1,- 1), (0, -1),
                                     (0, 0), (1, 0)],

                            pos_x, 2,
                            '*')
        
class PecaT(Peca):
    def __init__(self, pos_x):
        super().__init__([           (0, -1),
                            (-1, 0), (0, 0), (1, 0)],

                            pos_x, 2,
                            '+')