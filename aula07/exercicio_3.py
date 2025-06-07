from typing import List

def filtrar_elementos_unicos(lista: List[int]) -> list:
    return list(set(lista))

if __name__ == '__main__':
    lista = [69, 8, 40, 90, 8, 9, 90, 13, 15, 15]
    print(filtrar_elementos_unicos(lista=lista))