def ordenar_chaves_dicionario(dicionario: dict) -> list:
    return sorted(dicionario.keys())

if __name__ == '__main__':
    dicionario = {'nome': 'Maria', 'idade': 35, 'setor': 'Marketing','genero': 'F', 'uf': 'DF'}
    print(ordenar_chaves_dicionario(dicionario=dicionario))