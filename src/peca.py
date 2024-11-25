import random

class Peca:
    def __init__(self, blocos, x, y, caractere):
        self.blocos = blocos
        self.x = x
        self.y = y
        self.caractere = caractere
        
    @staticmethod
    def gerar_peca_aleatoria(centro):
        tipos_de_pecas = [PecaO, PecaI, PecaL, PecaJ, PecaS, PecaZ, PecaT]
        return random.choice(tipos_de_pecas)(centro)



##########################################################
################### SUBCLASSES DE PEÇA ###################

class PecaO(Peca):
    def __init__(self, pos_x):
        super().__init__([  (-0.5, -0.5), (0.5, -0.5),
                            (0.5, 0.5), (-0.5, 0.5)],

                            pos_x + 0.5, 1.5,
                            '@')

class PecaI(Peca):
    def __init__(self, pos_x):
        super().__init__([  (-1.5, -0.5), (-0.5, -0.5), (0.5, -0.5), (1.5, -0.5)],
                         
                            pos_x + 0.5, 1.5,
                            '$')
        
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

