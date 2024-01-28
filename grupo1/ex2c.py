# Função para verificar o gênero com base na letra digitada
def verificar_genero(letra):
    if letra.upper() == 'F':
        return "Feminino"
    elif letra.upper() == 'M':
        return "Masculino"
    else:
        return "Sexo Inválido"


letra_digitada = input("Digite 'F' para Feminino ou 'M' para Masculino: ")

# Verificar e exibir o gênero correspondente
genero = verificar_genero(letra_digitada)
print(f"O gênero correspondente à letra digitada é: {genero}")
