from typing import List

def somar_lista(lista: List[int | float]) -> int|float:
    return sum(lista)

if __name__ == '__main__':
    lista = list(range(1,15))
    print(somar_lista(lista))