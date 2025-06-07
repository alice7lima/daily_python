from typing import List

def filtrar_valores_por_limite(lista: List[int], limite: int) -> list:
    return [valor for valor in lista if valor > limite]

if __name__ == '__main__':
    lista = [2, 20, 40, 60, 8, 100, 90]
    limite = 30

    print(filtrar_valores_por_limite(lista=lista, limite=limite))