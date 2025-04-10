def calcular_media(nota1, nota2):
    try:
        nota1 = float(nota1)
        nota2 = float(nota2)
        return (nota1 + nota2) / 2
    except ValueError:
        return None
