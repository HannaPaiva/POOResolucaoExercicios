
def verificar_situacao(nota1, nota2):

    media = (nota1 + nota2) / 2

    if media >= 19:
        return "Aprovado com Distinção"
    elif media >= 9.5:
        return "Aprovado"
    else:
        return "Reprovado"


try:
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
except ValueError:
    print("Por favor, digite notas válidas.")
else:
    # Verificar e exibir a situação do aluno
    situacao = verificar_situacao(nota1, nota2)
    print(f"A situação do aluno é: {situacao}")
