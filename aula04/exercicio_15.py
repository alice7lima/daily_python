texto = "engenharia de dados"
frequencia = {}

for char in texto:
    if char not in frequencia:
        frequencia[char] = 1
    else:
        frequencia[char] += 1

print(frequencia)