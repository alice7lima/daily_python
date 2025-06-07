from typing import List

def calcula_media_lista(lista: List[int]) -> float:
    return round((sum(lista)/len(lista)), 2)

if __name__ == '__main__':
    lista = [5, 6, 9, 10, 11, 154, 7]
    print(calcula_media_lista(lista=lista))