def identificar_combinacoes(lista: list, numero: int) -> list:
    combinacoes = set()
    
    for num1 in lista:
        for num2 in lista:
            if num1 + num2 == numero:

                combinacoes.add(tuple(sorted((num1, num2))))

    return combinacoes

if __name__ == '__main__':
    lista = [1,2,3,4,5,6,7,8,9,10]
    print('Combinações possíveis:', identificar_combinacoes(lista=lista, numero=9))