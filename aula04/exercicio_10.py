valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
valores_pares = [l for l in valores if l%2 == 0]
valores_impares = [l for l in valores if l not in valores_pares]

print(f"Lista pares: {valores_pares}")
print(f"Lista ímpares: {valores_impares}")