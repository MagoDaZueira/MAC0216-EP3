import random

class Peca:
    def __init__(self, blocos: list[tuple], x: int, y: int, caractere: str):
        """Construtor da classe Peca.
        
        - Parâmetros:
        - - blocos - lista de tuplas contendo as posições (x, y) em relação ao centro da peça.
        - - x - posição horizontal do centro da peça no grid.
        - - y - posição vertical do centro da peça no grid.
        - - caractere - símbolo usado para mostrar esta peça na tela.
        """
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
    def gerar_peca_aleatoria(centro_x: int):
        """Escolhe aleatoriamente um dos possíveis tipos de peças,
        os quais são subclasses desta classe Peca, e cria essa
        peça no topo do tabuleiro.
        
        - Parâmetros:
        - - centro_x - Indica a posição horizontal do grid onde
        a peça deve surgir.

        Não retorna valores
        """

        tipos_de_pecas = [PecaO, PecaI, PecaL, PecaJ, PecaS, PecaZ, PecaT]
        return random.choice(tipos_de_pecas)(centro_x)
    
    
    def mover(self, dx: int, dy: int, grid: list[list[str]]) -> None:
        """Move a peça horizontalmente ou para baixo, caso possível
        
        - Parâmetros:
        - - dx - Desclocamento horizontal desejado.
        - - dy - Desclocamento vertical desejado.
        - - grid - Indica quais posições estão ocupadas, e quais livres.
        As posições livres devem ser dadas por ' '.

        Não retorna valores.
        """

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

    
    def rotacionar_direita(self, grid: list[list[str]]) -> None:
        """Rotaciona a peça para a direita, caso possível.
        
        - Parâmetros:
        - - grid - Indica quais posições estão ocupadas, e quais livres.
        As posições livres devem ser dadas por ' '.

        Não retorna valores.
        """

        # Lista com novas posições pela fórmula adequada
        novos_blocos = [(-y, x) for (x, y) in self.blocos]

        # Faz os ajustes necessários, caso possíveis
        correcao = self.verificar_rotacao(novos_blocos, grid)

        # Se há algum ajuste válido, atualiza posição dos blocos
        if len(correcao):
            self.blocos = [(x, y) for (x, y) in correcao]

            
    def rotacionar_esquerda(self, grid: list[list[str]]) -> None:
        """Rotaciona a peça para a esquerda, caso possível.
        
        - Parâmetros:
        - - grid - Indica quais posições estão ocupadas, e quais livres.
        As posições livres devem ser dadas por ' '.

        Não retorna valores.
        """

        # Lista com novas posições pela fórmula adequada
        novos_blocos = [(y, -x) for (x, y) in self.blocos]

        # Faz os ajustes necessários, caso possíveis
        correcao = self.verificar_rotacao(novos_blocos, grid)

        # Se há algum ajuste válido, atualiza posição dos blocos
        if len(correcao):
            self.blocos = [(x, y) for (x, y) in correcao]

    
    def verificar_rotacao(self, posicoes: list[tuple], grid: list[list[str]]) -> list:
        """Testa se a rotação é possível, usando uma lista de offsets
        para verificar se, caso a rotação padrão não seja possível,
        algum pequeno deslocamento a torna válida.

        - Parâmetros:
        - - posicoes - As novas posições relativas dos blocos ao pivô, após a rotação base
        - - grid - Indica quais posições estão ocupadas, e quais livres.
        As posições livres devem ser dadas por ' '.

        Retorna uma lista de tuplas com posições de blocos válidas,
        caso haja algum offset possível.
        Caso não exista offset válido, retorna uma lista vazia.
        
        """
        for offset in self.offsets_rotacao:
            offset_valido = True
            novas_pos = [(pos[0] + offset[0], pos[1] + offset[1]) for pos in posicoes]

            for bloco in novas_pos:
                # Posições dos blocos no grid
                new_x = round(self.x + bloco[0])
                new_y = round(self.y + bloco[1])

                # Garante que não tenha saído do tabuleiro
                if new_x >= len(grid[0]) or new_y >= len(grid):
                    pode_mover = False

                # Verifica se posição com offset é válida
                elif grid[new_y][new_x] != ' ':
                    offset_valido = False
            
            if offset_valido:
                return novas_pos
        
        return []


##########################################################
################### SUBCLASSES DE PEÇA ###################

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