# Número de pessoas
num_pessoas = 2


idades = []
alturas = []

for i in range(num_pessoas):
    try:
        idade = int(input(f"Digite a idade da pessoa {i + 1}: "))
        altura = float(input(f"Digite a altura da pessoa {i + 1} em metros: "))


    except ValueError:
        print("Por favor, digite valores válidos.")
        break
    else:
        idades.append(idade)
        alturas.append(altura)

print("\nIdades e Alturas na Ordem Inversa:")
for i in range(num_pessoas - 1, -1, -1):
    print(f"Pessoa {i + 1}: Idade - {idades[i]}, Altura - {alturas[i]:.2f} metros")
