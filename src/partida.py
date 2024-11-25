class Partida:
    
    def __init__(self, nome, linhas, colunas):
        self.nome = nome
        self.linhas = linhas
        self.colunas = colunas
        self.grid_draw = [[' ' for _ in range(colunas)] for _ in range(linhas)]

    def mostrar_tela(self):
        for linha in self.grid_draw:
            for caractere in linha:
                print(caractere, end=" ")
            print()
            