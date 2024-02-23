BONUS_2024 = 1000

nome_valido = False
salario_valido = False
bonus_valido = False
#recebe as informacoes do usuario

while not nome_valido:
    try:
        nome = input("Bem vind@! Digite o seu nome: ")
        if any(letra.isdigit() for letra in nome):
            raise ValueError("ERRO: O nome não deve conter números.")
        elif any(not letra.isalpha() for letra in nome):
            raise ValueError("ERRO: O nome não deve conter caracteres especiais.")
        elif nome.isspace() or len(nome) == 0:
            raise ValueError("ERRO: O nome não pode ser vazio.")
        
        else:
            nome_valido = True
        
    except ValueError as e:
        print(e)

    
while not salario_valido:  
    try:
        salario = float(input("Digite o seu salário: "))

        if salario < 0:
            print("ATENÇÃO: O salário não pode ser negativo.")
            raise ValueError
        
        else:
            salario_valido = True
        
    except ValueError as e:
        print("ERRO: O formato do salário informado não é válido, digite um número.")

while not bonus_valido:
    try:
        bonus = float(input("Digite o valor do bônus recebido: "))

        if bonus < 0:
            print("ATENÇÃO: O bônus não pode ser negativo.")
            raise ValueError
        
        else:
            bonus_valido = True
        
    except ValueError as e:
        print("ERRO: O formato do bônus informado não é válido, digite um número.")

#calcula o kpi
kpi_bonus = BONUS_2024 + salario * bonus

#exibe os resultados
print(f"O usuário {nome.capitalize()} possui o bonus de {kpi_bonus}")

print(f"O salário do usuário {nome.capitalize()} é R$ {salario} e o bonus é de {bonus}")
