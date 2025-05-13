def verificar_primo(numero: int) -> bool:
    if numero <= 1:
        return False
    
    for i in range(2, numero):
        if numero % i == 0:
            return False
        
    return True

if __name__ == '__main__':
    numero = 27

    if verificar_primo(numero):
        print(f"{numero} é primo")
    else:
        print(f"{numero} não é primo")