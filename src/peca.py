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
    
    def mover(self, dx, dy, grid):
        pode_mover = True
        for bloco in self.blocos:
            new_x = round(self.x + bloco[0]) + dx
            new_y = round(self.y + bloco[1]) + dy

            print(new_x, new_y)

            if grid[new_y][new_x] != ' ':
                pode_mover = False
            
        if pode_mover:
            self.x += dx
            self.y += dy


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