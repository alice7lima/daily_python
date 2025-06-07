from typing import List

def encontrar_valores_faltantes(lista: List[int]) -> List[int]:
    lista_completa = set(range(min(lista), max(lista) + 1))
    return list(lista_completa - set(lista))


if __name__ == '__main__':
    lista = list(set(range(1,3)) | set(range(7,11)))
    print(encontrar_valores_faltantes(lista=lista))