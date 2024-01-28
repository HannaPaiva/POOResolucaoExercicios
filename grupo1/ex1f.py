# area do quadrado = lado * lado
# perimetro = lado * 4

while True:
    try:
        lado = float(input("Digite o lado do quadrado "))
        break

    except:
        print("\n O valor do lado não é válido! \n")


area = lado * lado
perimetro = lado*4

print(f"Com o lado {lado}, a área do quadrado é: {round(area, 3)} ")
print(f"Com o lado {lado}, o perímetro do quadrado é: {round(perimetro, 3)} ")


