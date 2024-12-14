# MAC0216-EP3

## Integrantes da dupla:
### Otávio Garcia Capobianco
- NUSP: 15482671
- email: gcotavio@usp.br

### João Victor Fernandes de Sousa
- NUSP: 15495651
- email: joaovictor.fernandes@usp.br

## Como o Programa Funciona
O programa consiste de uma versão de tetris que executa no terminal, substituindo os sprites por caracteres, por isso, Textris.
Resumidamente, há o arquivo principal ````main.py```, onde está implementada a classe Jogo, que administra o uso das demais funcionalidades do jogo, chamando as partidas, o carregamento de saves e o ranking das dez melhores pontuações.
### Partida
A classe Partida, como o próprio nome sugere, implementa uma rodada de Textris. Cada vez que o jogador inicia uma nova partida, uma nova instância de Partida é criada, tendo como argumentos as dimensões do grid e o nome do jogador. A partir disso, as peças são manipuladas através da classe Peca. Para salvar a partida, a instância atual de Partida é salva em um arquivo através da biblioteca pickle.
### Peca
A classe Peca implementa os métodos de manipulação das peças do Textris. Ela armazena métodos para rotacionar as peças, desenhá-las e movê-las. Além disso, há subclasses para cada possível formato de peça, o que é necessário, já que cada formato de peça possui uma distância diferente dos seus blocos em relação ao pivô e um caractere diferente em seu desenho.

## Testes
O programa também contém testes unitários para verificação da funcionalidade dos principais métodos. 
Para a classe Partida, foi implementada uma classe TestPartida, que testa os principais métodos relacionados à funcionalidade da Partida, com exceção de métodos que são réplicas de métodos da classe Peca ou que não sejam muito relevantes.
Para a classe Peca, foi implementada uma classe TestPeca, que verifica o movimento e rotação das peças. 
Além disso, foi implementado um teste para a impressão de pontuações no arquivo do ranking, através da classe TestRanking.

## Como Executar
Para executar o programa, pode-se navegar até a parta ```src``` e executar o programa ```main.py```, através do comando:
```python
python main.py
```
Ou:
```python
python3 main.py
```
Para a execução dos testes e geração da documentação com o Doxygen, basta executar no terminal:
 ```bash
 make all
 ```
 Para somente a execução dos testes:
 ```bash
 make tests
 ```
 Ou, para gerar somente a documentação:
 ```bash
 make doc
 ```
 Finalmente, para limpar os arquivos intermediários dessas execuções, faça:
 ```bash
 make clean
 ```

## Dependências
Para a utilização da geração de documentação e testes automatizados, é preciso ter instalado o make e doxygen. Se estiver usando linux em distribuições baseadas em Debian/Ubuntu, execute:
```bash
sudo apt install make
sudo apt install doxygen
```
Esse programa é escrito em python, sendo necessário usar a versão 3.9 ou superior para aproveitá-lo sem problemas. Além disso, tem como dependências as bibliotecas readchar e pytest. Você pode instalá-las pelo terminal usando:
```bash
pip install pytest readchar
```
Ou, se preferir, utilizar:
```bash
make requirements
```
O programa foi testado em Windows/WSL e MacOS, utilizando a versão 3.10.12, 3.11 e 3.12.8. É necessário usar a versão 3.9 ou superior, devido à falta de suporte à sintaxe usada em alguns trechos do código em versões anteriores. Para verificar a versão do python utilizada, basta inserir o comando:
```python
python --version
```
Ou:
```python
python3 --version
```


