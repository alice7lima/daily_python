from typing import List
from math import sqrt

def calcular_desvio_padrao(lista: List[float]) -> float:
    media_aritmetica = sum(lista)/len(lista)
    somatorio = sum([(valor - media_aritmetica)** 2 for valor in lista])

    return f"{sqrt(somatorio/len(lista)):.2f}"


if __name__ == '__main__':
    lista = [1, 12, 3, 14, 15, 6, 7, 8, 9, 4]
    print(calcular_desvio_padrao(lista=lista))