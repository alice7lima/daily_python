ocorrencias = dict()
string = 'abracadabra abracadaaabraaa'

for char in string:
    if char not in ocorrencias:
        ocorrencias[char] = 1
    else:
        ocorrencias[char] += 1

print(ocorrencias)