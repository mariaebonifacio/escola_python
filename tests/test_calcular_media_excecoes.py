import pytest
from escola.aluno import calcular_media

def test_calcular_media_lista_vazia():
    # Definindo a entrada
    entrada = []

    # Executando a função e esperando erro
    with pytest.raises(ValueError, match="não é permitido uma lista vazia"):
        calcular_media(entrada)

def test_calcular_media_enviando_string():
    #define entrada
    entrada = "Olá"

    #executando a função e esperando erro
    with pytest.raises(ValueError, match="não é permitido uma lista com textos"):
        calcular_media(entrada)

def test_calcular_media_enviando_string():
    #definindo entrada
    entrada = ["Olá"]

    # Executando a função e esperando erro
    with pytest.raises( ValueError, match="nota inválida"):
        calcular_media(entrada)

# --------------------------------------------------------------------------------

# enviando string como nota
def test_calcular_media_enviando_string_como_nota(notas:list[float]) -> float:
    # definindo a entrada
    entrada = [(3.0), 2.0]

    # Executando a função esperando dar erro
    with pytest.raises(ValueError, match="nota inválida"):
        calcular_media(entrada)

# --------------------------------------------------------------------------------

def test_media_com_numero_negativo():
    #definindo a entrada
    entrada =[-10.0]
    
    # executando a função e esperando erro
    with pytest.raises(ValueError, match="não é permitido uma lista com números negativos"):
        calcular_media(entrada)

