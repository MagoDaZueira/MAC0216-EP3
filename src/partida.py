class Partida:
    
    def __init__(self, nome, linhas, colunas):
        self.nome = nome
        self.linhas = linhas
        self.colunas = colunas

        # Desenha o layout inicial
        self.grid_draw = [
            [
                '_' if i == 0 or i == linhas - 1 else
                '|' if j == 0 or j == colunas - 1 else ' '
                for j in range(colunas)
            ]
            for i in range(linhas)
        ]

        # Bordas arredondadas
        self.grid_draw[0][0]                = ' '
        self.grid_draw[linhas-1][0]         = ' '
        self.grid_draw[0][colunas-1]        = ' '
        self.grid_draw[linhas-1][colunas-1] = ' '

        self.mostrar_tela()

    def mostrar_tela(self):
        """Imprime os elementos presentes no jogo,
        baseado na matriz self.grid_draw"""
        for linha in self.grid_draw:
            for caractere in linha:
                print(caractere, end=" ")
            print()
            