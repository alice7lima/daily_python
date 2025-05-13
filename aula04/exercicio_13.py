estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

estoque = {produto: quantidade for produto, quantidade in estoque.items() if quantidade > 0}

print(estoque)