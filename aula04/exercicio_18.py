def inverter_string(frase: str) -> str:
    return frase[::-1]

if __name__ == '__main__':
    frase = 'suco de cajá é bom'
    print(inverter_string(frase))