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

