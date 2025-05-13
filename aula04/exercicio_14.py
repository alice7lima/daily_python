dicionario = {"a": 1, "b": 2, "c": 3}

chaves_dicionario = [chave for chave in dicionario.keys()]
valores_dicionario = [valor for valor in dicionario.values()]

#alternativa
# chaves = list(dicionario.keys())
# valores = list(dicionario.values())

print(f"Chaves do dicionário: {chaves_dicionario}")
print(f"Valores do dicionário: {valores_dicionario}")