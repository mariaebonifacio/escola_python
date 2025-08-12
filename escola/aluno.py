# Calculo básico

def calcular_media(entrada:list[float]) -> float:

    """" 
    Calcula a média de uma lista de notas

    Parâmetros:
    notas (list[float]): Lista de notas a serem calculadas.

    Retorna:
    float: A média das notas, arredonda para uma casa decimal.
    """

    # Validando se a entrada é uma lista
    if not isinstance(entrada, list):
        raise TypeError("Nota inválifa")

    # Validando se a lista é vazia
    if len(entrada) == 0:
        raise ValueError("Não é permitido uma lista vazia")
        
    media = sum(entrada)/len(entrada)
    return round(media,1)
