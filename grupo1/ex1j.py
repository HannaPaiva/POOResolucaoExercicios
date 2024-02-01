# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em
# metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro
# para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam
# 80 euros. Informe ao utilizador da quantidades de latas de tinta a serem compradas e o
# preço total.

print("********************************************")
print("BEM VINDO À LOJA DE TINTAS!")
print("********************************************")

import math


def calcular_tinta_e_preco(metros_quadrados):

    cobertura_por_litro = 3#metros quadrados


    litros_necessarios = metros_quadrados / cobertura_por_litro


    latas_necessarias = math.ceil(litros_necessarios / 18) #menor número inteiro maior ou igual ao número

    preco_total = latas_necessarias * 80

    return latas_necessarias, preco_total

def obter_tamanho_area():
    while True:
        try:
            metros_quadrados = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
            return metros_quadrados
        except ValueError:
            print("Por favor, digite um valor válido.")


tamanho_area = obter_tamanho_area()

# Calcular a quantidade de latas de tinta e o preço total 
latas_necessarias, preco_total = calcular_tinta_e_preco(tamanho_area)

print(f"Você precisará de {latas_necessarias} latas de tinta, e o preço total será de {preco_total} euros.")
