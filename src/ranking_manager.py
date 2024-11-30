import os
import textos as txt

def atualizar_ranking(nome, pontuacao):
    os.makedirs('./ranking', exist_ok=True)
    if not(os.path.exists('./ranking/ranking.txt')):
        with open(f'./ranking/ranking.txt', 'w') as arquivo:
            pass
            
    with open('./ranking/ranking.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        linhas.reverse()
        print(linhas)
        if len(linhas) < 5:
                linhas.append(f"{nome} {pontuacao}\n")
        else:
            for i, linha in enumerate(linhas[:-1]):
                linha_separada = linha.split()
                if pontuacao > int(linha_separada[1]):
                    linhas[i] = f"{nome} {pontuacao}\n"
                    break
        
    linhas = sorted(linhas, key=lambda linha: int(linha.strip().split()[1]), reverse=True)
    with open(f'./ranking/ranking.txt', 'w') as arquivo: 
        arquivo.writelines(linhas)


def mostrar_ranking():
    os.makedirs('./ranking', exist_ok=True)
    try:
        with open(f'./ranking/ranking.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            print(txt.ranking)

            i = 1
            for linha in linhas:
                print(f'{i}) {linha}')
                i += 1

    except FileNotFoundError:
        with open('./ranking/ranking.txt', 'w') as arquivo:
            print('Ainda não há pontuações registradas, se esforce mais')