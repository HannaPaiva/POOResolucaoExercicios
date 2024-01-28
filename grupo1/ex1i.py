def calcular_peso_ideal(altura, genero):
    if genero.lower() == 'm':
        peso_ideal = 72.7 * altura - 58
    elif genero.lower() == 'f':
        peso_ideal = 62.1 * altura - 44.7
    else:
        print("Gênero inválido. Por favor, insira 'm' ou 'f'.")
        return None
    
    return peso_ideal

# Função para receber a altura e o gênero do usuário
def obter_dados():
    while True:
        try:
            altura = float(input("Digite a altura em metros: "))
            genero = input("Digite o gênero (m/f): ")
            return altura, genero
        except ValueError:
            print("Por favor, digite uma altura válida.")



altura, genero = obter_dados()


peso_ideal = calcular_peso_ideal(altura, genero)

if peso_ideal is not None:
    print(f"O peso ideal para uma pessoa de {altura} metros de altura e gênero {genero} é {peso_ideal:.2f} kg.")
