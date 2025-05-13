dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"c": 3, "d": 4}

dicionario_final = dict()
dicionario_final.update(dicionario1)
dicionario_final.update(dicionario2)

#alternativa
#dicionario_fundido = {**dicionario1, **dicionario2}

print(dicionario_final)