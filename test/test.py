# Projeto: Fluxo de CI/CD Prático
# Desenvolvedor: maedcozy (Maria Chaves)
# Disciplina: DevOps

from src.main import read_root, soma, subtracao, multiplicacao, divisao

def test_read_root():
    assert read_root() == {"Hello": "Bangtan!"}

def test_soma():
    assert soma(10, 5) == 15
    assert soma(-1, 1) == 0

def test_subtracao():
    assert subtracao(10, 5) == 5
    assert subtracao(5, 10) == -5

def test_multiplicacao():
    assert multiplicacao(10, 5) == 50
    assert multiplicacao(0, 5) == 0

def test_divisao():
    assert divisao(10, 2) == 5
    assert divisao(10, 0) == "Erro: Divisão por zero"