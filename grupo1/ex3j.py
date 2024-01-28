
def contar_pares_impares(numeros):
    pares = 0
    impares = 0

    for numero in numeros:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

    return pares, impares

numeros = []
for i in range(10):
    try:
        numero = int(input(f"Digite o {i + 1}º número inteiro: "))
        numeros.append(numero)
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

quantidade_pares, quantidade_impares = contar_pares_impares(numeros)

print(f"Quantidade de números pares: {quantidade_pares}")
print(f"Quantidade de números ímpares: {quantidade_impares}")
