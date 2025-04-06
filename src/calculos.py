import numpy as np

def calcular_media(notas):
    return np.mean(notas)

def calcular_aprovacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"
