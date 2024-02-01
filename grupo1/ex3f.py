# print("Insira 3 números para saber o maior entre eles")

# n1 = float(input("insira o primeiro: "))

# n2 = float(input("insira o segundo: "))

# n3 = float(input("insira o terceiro: "))

# maior = max(n1, n2, n3)

# print(f"O maior número entre [{n1}, {n2}, {n3}] é {maior}")


# Faça um programa que leia n números e informe a soma e a média destes.

valores = []

qtos = int(input("Quantos números deseja inserir? "))

for contador in range(1, qtos+1):

    variavel = float(input(f"Digite o {contador}º número: "))
    
    valores.append(variavel)
    

soma = sum(valores)

media = soma/qtos

print(f"para os valores: {valores}")

print(f"A soma de todos é: {soma}")

print(f"A média de todos é: {media}")
