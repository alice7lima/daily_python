lista_de_compras = ["maçã", "banana", "cereja"]
precos_produtos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
valor_compra = 0

for item in lista_de_compras:
    try:
        valor_compra += precos_produtos[item]
    except:
        print(f"O produto '{item}' não se encontra no dicionário dos preços.")

print(f"Total da compra: {valor_compra}")

#alternativa
# total = sum(precos_produtos[item] for item in lista_de_compras if item in precos_produtos)
# print(f"Total da compra: {total}")