# Makefile

# Alvo principal que executa todos os processos
all: tests doc

# Alvo para a documentação

doc: 
	doxygen Doxyfile

# Alvo para rodar os testes
tests:
	python3 -m pytest partida_test.py peca_test.py ranking_test.py

# Alvo para limpar arquivos intermediários
clean:
	rm -rf docs/ *.pyc __pycache__ .pytest_cache