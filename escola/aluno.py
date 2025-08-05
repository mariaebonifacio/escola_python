# Calculo básico

def calcular_media(notas:list[float]) -> float:

    # Verificando se é uma lista
    if not isinstance(notas, list[float]):
        raise ValueError("as notas não são uma lista.")

    # Validando se a lista é vazia
    if len(notas) == 0:
        raise ValueError("não é permitido uma lista vazia.")
    
    media = sum(notas)/len(notas)
    return round(media,1)
