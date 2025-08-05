import pytest
from escola.aluno import calcular_media

@pytest.mark.parametrize("entrada, situacao_esperada", 
                         [
                              ([0.0, 0.0, 0.0, 0.0], 0),                         #Calculo basico com notas apenas 0
                              ([10.0, 10.0, 10.0, 10.0], 10),                    #Calculo basico com notas apenas 10
                              ([7.0], 7.0),                                      #Calculo básico com apenas 1 nota
                              ([5.0, 8.8, 5.3, 6.4, 7.2, 2.8, 9.3], 6.4),      #Calculo básico com 7 notas
                              ([5.8, 9.3], 7.6),                               #Testando o arredondamento decimal maior que 0.55
                              ([0.8, 0.0, 0.0], 0.3),                          #Testando o arredondamento decimal maior que 0.56
                              ([5.0, 6.0, 7.0], 6.0)                           #Testando números inteiros
                         ]
                         )

def test_calcular_media_calculos_basicos_parametrizados(entrada, situacao_esperada):
    resultado = calcular_media(entrada)

    assert resultado == situacao_esperada