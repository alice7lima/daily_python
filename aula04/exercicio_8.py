def criterio_ordenacao(elemento):
    return elemento['nome']

pessoas = [
{"nome": "Alice", "idade": 30},
{"nome": "Yara", "idade": 26},
{"nome": "Bob", "idade": 25},
{"nome": "Carol", "idade": 20}
]

pessoas.sort(key=criterio_ordenacao)
#alternativa
#pessoas.sort(key=lambda pessoa: pessoa['nome'])
print(pessoas)