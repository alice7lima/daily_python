BONUS_2024 = 1000

#recebe as informacoes do usuario
nome = input("Bem vind@! Digite o seu nome: ")

salario = float(input("Digite o seu salário: "))

bonus = float(input("Digite o seu bônus: "))

#calcula o kpi
kpi_bonus = BONUS_2024 + salario * bonus

#exibe os resultados
print(f"O usuário {nome} possui o bonus de {kpi_bonus}")

print(f"O salário do usuário {nome} é R$ {salario} e o bonus é de {bonus}")